from django.contrib import messages
from datetime import timedelta
import smtplib
from email.message import EmailMessage

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Ordem, Etapa, motivoParada
from django.utils import timezone
from django.db.models import Count

#Funcão para envio de e-mails seguindo critérios de etapas
def enviaEmail(etapa, numero, ordem, et):
    EMAIL_ADREE = 'etapafinalizada@gmail.com'
    SENHA_ADREE = 'tjwnwnzxgkwkzvlj'
    msg = EmailMessage()
    
    msg['From'] = 'etapafinalizada@gmail.com'
    msg['To'] = 'etapafinalizada@gmail.com'

    if str(etapa) == '2':
        msg['Subject'] = f'Status Etapa 1 - OS {numero}'
        mensagem = (f'A etapa 1, OS nº {numero} foi finalizada. Teste de pressão concluído.\n'
                    f'Cliente: {ordem.cliente}\n'
                    f'Modelo: {ordem.modelo}\n'
                    f'Tipo de Serviço: {ordem.get_tipo_display()}\n\n'
                    f'Observações Ordem: {ordem.obs_ordem}\n\n'
                    f'Observações Etapa: {et.obs_etapa}')
        msg.set_content(mensagem)
    if str(etapa) == '3':
        msg['Subject'] = f'Status Etapa 3 - OS {numero}'
        mensagem = (f'A etapa 3, OS nº {numero}  foi concluida. Serviço finalizado\n'
                    f'Cliente: {ordem.cliente}\n'
                    f'Modelo: {ordem.modelo}\n'
                    f'Tipo de Serviço: {ordem.get_tipo_display()}\n\n'
                    f'Observações Ordem: {ordem.obs_ordem}\n\n'
                    f'Observações Etapa: {et.obs_etapa}')
        msg.set_content(mensagem)
    if str(etapa) == '0':
        msg['Subject'] = f'Retrabalho - OS {numero}'
        mensagem = (f'Essa OS é um retrabalho, os nº {numero}\n'
                    f'Cliente: {ordem.cliente}\n'
                    f'Modelo: {ordem.modelo}\n'
                    f'Tipo de Serviço: {ordem.get_tipo_display()}\n\n'
                    f'Observações: {ordem.obs_ordem}')
        msg.set_content(mensagem)
    if str(etapa) == '1':
        msg['Subject'] = f'Garantia - OS {numero}'
        mensagem = (f'Essa OS é uma garantia, os nº {numero}\n'
                    f'Cliente: {ordem.cliente}\n'
                    f'Modelo: {ordem.modelo}\n'
                    f'Tipo de Serviço: {ordem.get_tipo_display()}\n\n'
                    f'Observações: {ordem.obs_ordem}')
        msg.set_content(mensagem)
    if str(etapa) == '5':
        msg['Subject'] = f'Status Etapa 2 - OS {numero}'
        mensagem = (f'A etapa 2, OS nº {numero} foi finalizada, prossiga com os trâmites de valores.\n'
                    f'Cliente: {ordem.cliente}\n'
                    f'Modelo: {ordem.modelo}\n'
                    f'Tipo de Serviço: {ordem.get_tipo_display()}\n\n'
                    f'Observações Ordem: {ordem.obs_ordem}\n\n'
                    f'Observações Etapa: {et.obs_etapa}')
        msg.set_content(mensagem)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADREE, SENHA_ADREE)
        smtp.send_message(msg)
#Fim da funcão de enviar e-mails

#Funcão que calcula o tempo decorrido
def calcula(inicio, fim):
    h1 = str(inicio)[11:13]
    m1 = str(inicio)[14:16]
    h2 = str(fim)[11:13]
    m2 = str(fim)[14:16]
    decorido = (int(h2) * 60 + int(m2)) - (int(h1) * 60 + int(m1))
    print(decorido)
    return decorido
#Fim da função de calcular o tempo

@login_required
def index(request):
    try:
        x = Ordem.objects.raw(
            'select _or.base_ptr_id, _or.vendedor_id, _or.tipo,_or.numeros,'
            '_eta.fase,_eta.media,_eta.inicio,_eta.decorrido,_eta.parado,_eta.id_ordem_id ,_eta.mostrar, f.nome, _eta.status,  '
            '_eta.base_ptr_id as meuid,mm.modelo as carro from home_ordem as _or '
            'join home_etapa as _eta on(_eta.id_ordem_id = _or.base_ptr_id)'
            'join home_modelo as mm on(mm.id = _or.modelo_id) '
            'join home_funcionario as f on(f.base_ptr_id = _eta.operador_id) '
        )
    except:
        return render(request, 'home/erro.html')

    return render(request, 'home/index.html', {'dados': x})

#Função que realiza a pausa durante a execução das etapas
@login_required
def parar(request, id):
    dados = Etapa.objects.get(id=id)
    # mParada = motivoParada.objects.get(id=id)
    # mParada.quantidadeParadas += 1
    # if request.POST.get('almoco'):
    #     mParada.almoco = request.POST.get('almoco')
    #     dados.parado += 0
    # if request.POST.get('fim_de_turno'):
    #     mParada.fim_de_turno = request.POST.get('fim_de_turno')
    #     dados.parado += 0
    # if request.POST.get('setup'):
    #     mParada.setup = request.POST.get('setup')
    #     dados.parado += calcula(dados.parada, dados.retomada)
    # if request.POST.get('outros'):
    #     mParada.outros = request.POST.get('outros')
    #     dados.parado += calcula(dados.parada, dados.retomada)

    dados.status = '8'
    dados.mostrar = '1'
    dados.parada = timezone.now()  #salva o tempo da parada
    dados.decorrido = calcula(dados.inicio, dados.parada) - dados.parado
    dados.save()
    messages.success(request, "Até logo!")
    return redirect('home')
#Fim da função de pausa

@login_required
def atualisa_status(request):
    id_etapa = int(request.POST.get('idetapa'))
    dados = Etapa.objects.get(id=id_etapa)

    if dados.operador_id == 133:   
        messages.success(request, "Por favor, indique um operador para iniciar o trabalho.")
        if dados.fase == '2':
            dados.status = '6'
        elif dados.fase == '3':
            dados.status = '3'

        return redirect('home')

#Rotina de início da da primeira etapa
    if dados.status == '0' and dados.fase == '1':
        dados.status = '1'
        dados.inicio = timezone.now()
        dados.save()
        messages.success(request, "Etapa um iniciada com sucesso.")
        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.status = '1'
        if final.tipo == 'R':
            enviaEmail('0', final.numeros, final, dados)
        if final.tipo == 'G':
            enviaEmail('1', final.numeros, final, dados)
        final.save()
    elif dados.status == '1' and dados.fase == '1':
        dados.status = '0'
        dados.mostrar = '0'
        dados.fim = timezone.now()
        if request.POST.get('limpesa'):
            dados.limpesa = request.POST.get('limpesa')
        if request.POST.get('conserto'):
            dados.conserto = request.POST.get('conserto')
        if request.POST.get('caixasup'):
            dados.caixa_sup = request.POST.get('caixasup')
        if request.POST.get('caixainf'):
            dados.caixa_inf = request.POST.get('caixainf')
        if request.POST.get('elemento'):
            dados.elemento = request.POST.get('elemento')
        if request.POST.get('bocal'):
            dados.bocal = request.POST.get('bocal')
        if request.POST.get('radiador'):
            dados.rad_novo = request.POST.get('radiador')
        if request.POST.get('colmeia'):
            dados.colmeia = request.POST.get('colmeia')

        dados.decorrido = calcula(dados.inicio, timezone.now())
        dados.status = '3'
        dados.save()

        id_ordem = dados.id_ordem_id
        final = Etapa.objects.filter(
            id_ordem_id=id_ordem, fase='2'
        )
        # Verifica se o trabalho realizado é um radiador novo e encerra as outras etapas
        if dados.rad_novo == 'S':
            messages.success(request, "Radiador novo finalizado!")
            dados_dois = Etapa.objects.get(base_ptr_id=final[0].id)
            dados_dois.status = '3'
            dados_dois.inicio = timezone.now()
            dados_dois.fim = timezone.now()
            dados_dois.decorrido = '0'
            dados_dois.rad_novo = 'S'
            dados_dois.operador = dados.operador
            dados_dois.save()
            final = Ordem.objects.get(base_ptr_id=id_ordem)
            final.status = '3'
            final.data_entrega = timezone.now()
            final.save()

            id_ordem = dados.id_ordem_id
            final = Etapa.objects.filter(
            id_ordem_id=id_ordem, fase='3'
        )   
            dados_tres = Etapa.objects.get(base_ptr_id=final[0].id)
            dados_tres.status = '3'
            dados_tres.inicio = timezone.now()
            dados_tres.fim = timezone.now()
            dados_tres.decorrido = '0'
            dados_tres.rad_novo = 'S'
            dados_tres.operador = dados.operador
            dados_tres.save()
            final = Ordem.objects.get(base_ptr_id=id_ordem)
            final.status = '3'
            final.data_entrega = timezone.now()
            final.save()

        else:
            dados_dois = Etapa.objects.get(base_ptr_id=final[0].id)
            dados_dois.mostrar = '1'
            dados_dois.status = '6'
            dados_dois.save()
            final = Ordem.objects.get(base_ptr_id=id_ordem)
            final.status = '2'
            final.save()

            messages.success(request, "Primeira etapa finalizada com sucesso.")
            enviaEmail('2', final.numeros,final, dados)
#Fim da rotina da primeira etapa

#Início da rotina da segunda etapa    
    #Rotina para a segunda etapa sem pausa
    elif dados.status == '6' and dados.fase == '2':
        dados.status = '2'
        dados.inicio = timezone.now()
        dados.save()
        messages.success(request, "Etapa dois inciada com sucesso.")
        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.status = '1'
        final.save()
    elif dados.status == '2' and dados.fase == '2':
        dados.status = '0'
        dados.mostrar = '0'
        dados.fim = timezone.now()
        dados.decorrido = calcula(dados.inicio, timezone.now()) - dados.parado
        dados.save()

        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.status = '2'
        final.save()

        id_ordem = dados.id_ordem_id
        final = Etapa.objects.filter(
            id_ordem_id=id_ordem, fase='3'
        )

        dados_tres = Etapa.objects.get(base_ptr_id=final[0].id)
        dados_tres.mostrar = '1'
        dados_tres.status = '3'
        dados_tres.save()
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        messages.success(request, "Etapa três disponível.")
        enviaEmail('5', final.numeros, final, dados)
    #Fim da rotina da segunda etapa sem pausa

    #Rotina de quando há uma parada na etapa 2    
    elif dados.status == '8' and dados.fase == '2' :    #Quando houver uma parada
        dados.retomada = timezone.now()                      #Atualiza o tempo atual
        dados.decorrido = calcula(dados.inicio, dados.parada) - dados.parado
        dados.parado += calcula(dados.parada, dados.retomada)
        # mParada = motivoParada.objects.get(id=id_etapa)
        # mParada.quantidadeParadas += 1
        # if request.POST.get('almoco'):
        #     mParada.almoco = request.POST.get('almoco')
        #     dados.parado += 0
        # if request.POST.get('fim_de_turno'):
        #     mParada.fim_de_turno = request.POST.get('fim_de_turno')
        #     dados.parado += 0
        # if request.POST.get('setup'):
        #     mParada.setup = request.POST.get('setup')
        #     dados.parado += calcula(dados.parada, dados.retomada)
        # if request.POST.get('outros'):
        #     mParada.outros = request.POST.get('outros')
        #     dados.parado += calcula(dados.parada, dados.retomada)
        # mParada.save()
        dados.status = '5'
        dados.save()
        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.status = '1'
        final.save()

        messages.success(request, "Etapa dois retomada com sucesso.")
    elif dados.status == '5' and dados.fase == '2' :
        dados.status = '0'
        dados.mostrar = '0'
        dados.fim = timezone.now()
        dados.decorrido = calcula(dados.inicio, dados.fim) - dados.parado #Calcula o tempo
        dados.save()
        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.status = '2'
        final.save()

        id_ordem = dados.id_ordem_id
        final = Etapa.objects.filter(
            id_ordem_id=id_ordem, fase='3'
        )

        dados_tres = Etapa.objects.get(base_ptr_id=final[0].id)
        dados_tres.mostrar = '1'
        dados_tres.status = '3'
        dados_tres.save()
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        messages.success(request, "Etapa três disponível após parada.")
        enviaEmail('5', final.numeros, final, dados)
    #fim da rotina de parada na etapa 2
#Fim da rotina a segunda etapa

#Inicio da rotina da terceira etapa
    #Rotina para a terceira etapa sem pausa
    elif dados.status == '3' and dados.fase == '3':
        dados.status = '4'
        dados.inicio = timezone.now()
        dados.save()
        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.status = '1'
        final.save()
        messages.success(request, "Etapa três inciada com sucesso.")
    elif dados.status == '4' and dados.fase == '3':
        dados.status = '0'
        dados.mostrar = '0'
        dados.fim = timezone.now()
        dados.decorrido = calcula(dados.inicio, timezone.now()) - dados.parado
        dados.save()
        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.status = '3'
        final.data_entrega = timezone.now()
        final.save()
        messages.success(request, "Finalizado.")
        enviaEmail('3', final.numeros, final, dados)
    #Fim da rotina da terceira etapa sem pausa

    #Rotina de quando há uma parada na etapa 3    
    elif dados.status == '8' and dados.fase == '3' :    #Quando houver uma parada
        dados.retomada = timezone.now()                        #Resgata o tempo da parada
        dados.decorrido = calcula(dados.inicio, dados.parada) - dados.parado
        dados.parado += calcula(dados.parada, dados.retomada)
        dados.status = '5'
        dados.save()
        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.status = '1'
        final.save()
        messages.success(request, "Etapa três retomada com sucesso.")
    elif dados.status == '5' and dados.fase == '3' :
        dados.status = '0'
        dados.mostrar = '0'
        dados.fim = timezone.now()
        dados.decorrido = calcula(dados.inicio, dados.fim) - dados.parado #Calcula o tempo
        dados.save()
        id_ordem = dados.id_ordem_id
        final = Ordem.objects.get(base_ptr_id=id_ordem)
        final.data_entrega = timezone.now()
        final.status = '3'
        final.save()
        messages.success(request, "Finalizado após parada.")
        enviaEmail('3', final.numeros, final, dados)
    #fim da rotina de parada na etapa 3
#Fim da rotina da terceira etapa
    else:
        pass
    return redirect('home')


@login_required
def dashboard(request):
    try:
        x = Ordem.objects.raw('select * from mostrar')
    except:
        return render(request, 'home/dashboard.html')

    result = (Ordem.objects
              .values('tipo')
              .annotate(dcount=Count('tipo'))
              .order_by()
              )
    ordem_by_operation = (Ordem.objects
                          .values('tipo')
                          .annotate(dcount=Count('tipo'))
                          .order_by()
                          )

    #print(result)
    context = {
        'dados': x,
        'tipo': result,
    }
    return render(request, 'home/dashboard.html', context)

#Funções para deletar linhas do banco de dados das Ordens e Etapas.
def deleta_etapas_antigas():
    d = timezone.now() - timedelta(days=185) #define como expiradas acima de 185 dias
    #chama as etapas expieradas
    etapas = Etapa.objects.filter(fim__lt=d)
    etapas.delete()
    
def deleta_ordens_antigas():
    d = timezone.now() - timedelta(days=185) #define como expiradas acima de 185 dias
    #chama as ordes expiradas

    ordens = Ordem.objects.filter(data_entrega__lt=d)
    ordens.delete()
#Fim das funções de exclusão
