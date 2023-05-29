

function mostar() {
    var dt = new Date();
    var tabela = document.getElementById('tbody');
    for (i = 0; i < tabela.rows.length; i++) {
        var linha = tabela.rows[i];
        // var produtoo = tabela.rows[i].cells[0];
        // var media = tabela.rows[i].cells[1];
        // var decorrido = tabela.rows[i].cells[2];
        // var status = tabela.rows[i].cells[3];

        var start = tabela.rows[i].cells[2].textContent.split(":");
        var atual = tabela.rows[i].cells[4].textContent.split(":");

        var init = start[0] * 60;
        var total_start = init + Number(start[1])

        var hora_atual = dt.getHours();
        var min_atual = dt.getMinutes();
        var ttotal_hora = hora_atual * 60 + min_atual


            tabela.rows[i].cells[3].innerHTML = ttotal_hora - total_start


        var media = Number(tabela.rows[i].cells[3].textContent)
        var TT = Number(tabela.rows[i].cells[1].textContent) / 2

        // verificar
        if (Number(tabela.rows[i].cells[3].textContent) >= Number(tabela.rows[i].cells[1].textContent)) {
            tabela.rows[i].cells[4].innerHTML = '<div style="color: red;font-weight: bold; font-size: 2rem;" >  Excedeu </div> '
        } else {
            if (media < TT) {
                tabela.rows[i].cells[4].innerHTML =
                    '<div style="color: green;font-weight: bold; font-size: 2rem;" >  Saldo ' +
                    String(Number(tabela.rows[i].cells[1].textContent) - Number(tabela.rows[i].cells[3].textContent))+' Min(s)'
            } else if( media >= TT) {
                tabela.rows[i].cells[4].innerHTML =
                    '<div style="color: orange;font-weight: bold; font-size: 2rem;" > Finaliza em ' +
                    String(Number(tabela.rows[i].cells[1].textContent) - Number(tabela.rows[i].cells[3].textContent))+' Min(s)'
            }

        }

        // fim ferificar

    }
}

setInterval(function () {
    mostar()
    console.log("Chamando ")
}, 2000);

