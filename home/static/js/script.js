

function mostar() {
    var dt = new Date();
    var tabela = document.getElementById('tbody');
    for (i = 0; i < tabela.rows.length; i++) {
        var linha = tabela.rows[i];

        /* decorrido -> tabela.rows[i].cells[3]
           status -> tabela.rows[i].cells[4]
           etapa.status -> tabela.rows[i].cells[6]
           etapa.decorrido -> tabela.rows[i].cells[7]
           etapa.parado -> tabela.rows[i].cells[8]
        */
        

        var start = tabela.rows[i].cells[2].textContent.split(":");
        var atual = tabela.rows[i].cells[4].textContent.split(":");

        var init = start[0] * 60;
        var total_start = init + Number(start[1])
        var parado = tabela.rows[i].cells[8].innerHTML

        var hora_atual = dt.getHours();
        var min_atual = dt.getMinutes();
        var ttotal_hora = hora_atual * 60 + min_atual

        if (Number(tabela.rows[i].cells[6].innerHTML) == '8')    
            tabela.rows[i].cells[3].innerHTML = tabela.rows[i].cells[7].innerHTML
        else
            tabela.rows[i].cells[3].innerHTML = ttotal_hora - total_start - parado


        var media = Number(tabela.rows[i].cells[3].textContent)
        var TT = Number(tabela.rows[i].cells[1].textContent) / 2

        // verificar
        if (Number(tabela.rows[i].cells[3].textContent) >= Number(tabela.rows[i].cells[1].textContent)) {
            tabela.rows[i].cells[4].innerHTML = '<div style="color: red;font-weight: bold; font-size: 2rem;" >  Excedeu </div> '
        } else {
            if (media < TT) {
                tabela.rows[i].cells[4].innerHTML =
                    '<div style="color: green;font-weight: bold; font-size: 2rem;" >  Restante ' +
                    String(Number(tabela.rows[i].cells[1].textContent) - Number(tabela.rows[i].cells[3].textContent))+' Min(s)'
            } else if( media >= TT) {
                tabela.rows[i].cells[4].innerHTML =
                    '<div style="color: orange;font-weight: bold; font-size: 2rem;" > Finaliza em ' +
                    String(Number(tabela.rows[i].cells[1].textContent) - Number(tabela.rows[i].cells[3].textContent))+' Min(s)'
            }

        }

        // fim verificar

    }
}

setInterval(function () {
    mostar()
    console.log("Chamando ")
}, 2000);

