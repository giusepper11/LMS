function CriaRadio(name, value, text, ident) {
    var label = document.createElement("label");
    var radio = document.createElement("input");
    radio.type = "radio";
    radio.name = name;
    radio.value = value;
    radio.id = ident;

    label.appendChild(radio);

    label.appendChild(document.createTextNode(text));
    return label;
}

function tableCreate() {
    var body = document.getElementsByTagName('dadosAluno')[0];
    var tbl = document.getElementById('tblAluno');
    tbl.style.width = '40%';
    tbl.setAttribute('border', '1');
    var tbdy = document.createElement('tbody');
    for (var i = 0; i < 60; i++) {
        var tr = document.createElement('tr');
        for (var j = 0; j < 2; j++) {
            var td = document.createElement('td');
            td.appendChild(document.createTextNode('Aluno1'+i));
            if (j == 1) {
                td.appendChild(CriaRadio("aluno" + i, "aprovado", "Aprovado", "alunoapr" + i))
                td.appendChild(CriaRadio("aluno" + i, "cancelado", "Cancelado", "alunocanc" + i))
            }
            tr.appendChild(td);
        }
        tbdy.appendChild(tr);
    }
    tbl.appendChild(tbdy);
}

function valida() {
    var contApr = 0;
    var contCanc = 0;
    for (var j = 0; j < 60; j++) {
        if (document.getElementById("alunoapr" + j).checked == true)
            contApr += 1;
        else if (document.getElementById("alunocanc" + j).checked == true)
            contCanc += 1;
    }
    alert('Aprovados: ' + contApr + '\nCancelados: ' + contCanc);
    if (contApr + contCanc >= 20)
        return true
    else
        alert('Você precisa selecionar no minimo 20 alunos.')
}

function validar() {
    var temp = 0;
    var nomecompleto = form1.nomecompleto.value;
    var senha = form1.pass.value;
    var conf_senha = form1.conf.value;
    var cpfnum = form1.cpfnum.value;
    var login = form1.login.value;
    var datanasc = form1.datanasc.value;
    var numeros, digitos, soma, i, resultado, digitos_iguais;
    // idade

    var MILLISECONDS_IN_A_YEAR = 1000 * 60 * 60 * 24 * 365;
    var date_array = datanasc.split('-');
    var years_elapsed = (new Date() - new Date(date_array[0], date_array[1], date_array[2])) / (MILLISECONDS_IN_A_YEAR);
    if (years_elapsed < 17) {
        alert('Idade Invalida');
        form1.datanasc.focus();
        temp = 1
        // return false;
    }
////////////////////////////////////////////////////////////
    //email
    var usuario = form1.email.value.substring(0, form1.email.value.indexOf("@"));
    var dominio = form1.email.value.substring(form1.email.value.indexOf("@") + 1, form1.email.value.length);
    if ((usuario.length >= 1) &&
        (dominio.length >= 3) &&
        (usuario.search("@") == -1) &&
        (dominio.search("@") == -1) &&
        (usuario.search(" ") == -1) &&
        (dominio.search(" ") == -1) &&
        (dominio.search(".") != -1) &&
        (dominio.indexOf(".") >= 1) &&
        (dominio.lastIndexOf(".") < dominio.length - 1)) {

    }
    else {
        alert("E-mail invalido");
        form1.email.focus();
        temp = 1
        // return false;
    }
/////////////////////////////////////////////////////////////////////////
    //nomecompleto
    if (nomecompleto == "") {
        alert('Preencha o campo com seu nome');
        form1.nomecompleto.focus();
        temp = 1
        // return false;
    }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //login
    if (login == "") {
        alert('Preencha o campo com seu login');
        form1.nomecompleto.focus();
        temp = 1
        // return false;
    }
//////////////////////////////////////////////////////////////////////

    //senha
    if (senha != conf_senha) {
        alert('Senhas diferentes');
        form1.senha.focus();
        temp = 1
        // return false;
    }

    if ((senha == "") && (conf_senha == "")) {
        alert('Preencha o campo com sua senha');
        form1.nomecompleto.focus();
        temp = 1
        // return false;
    }

    if (senha.search(/\d/) == -1) {
        alert('Senha invalida');
        temp = 1
        // return false;
    } else if (senha.search(/[a-zA-Z]/) == -1) {
        alert('Senha invalida');
        temp = 1
        // return false;
    }
    // return true;


    //////////////////////////////////////////////////////////////////////

    //CPF

    digitos_iguais = 1;
    if (cpfnum.length < 11) {
        alert('CPF invalido');
        temp = 1
        // return false;
    }
    for (i = 0; i < cpfnum.length - 1; i++)
        if (cpfnum.charAt(i) != cpfnum.charAt(i + 1)) {
            digitos_iguais = 0;
            break;
        }
    if (!digitos_iguais) {
        numeros = cpfnum.substring(0, 9);
        digitos = cpfnum.substring(9);
        soma = 0;
        for (i = 10; i > 1; i--)
            soma += numeros.charAt(10 - i) * i;
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(0)) {
            alert('CPF invalido');
            form1.cpfnum.focus();
            temp = 1
            // return false;
        }
        numeros = cpfnum.substring(0, 10);
        soma = 0;
        for (i = 11; i > 1; i--)
            soma += numeros.charAt(11 - i) * i;
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(1)) {
            alert('CPF invalido');
            form1.cpfnum.focus();
            temp = 1

            // return false;
        }
        // return true;
    }
    else {
        alert('CPF invalido');
        form1.cpfnum.focus();
        temp = 1
        // return false;
    }
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    if (temp == 0) {
        alert('Formulario enviado com sucesso')
    }

}