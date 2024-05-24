function gerar_tabuada() {
	var valor = document.getElementById('entry_valor').value;
	const elementos_criados = document.getElementsByClassName('valor_tabuada');
	var tamanho = Object.keys(elementos_criados).length;
	console.log('Quantidade elementos criados: '+tamanho);
	if (tamanho > 0) {
		//inserir código que remove valores anteriores!
		//elementos_criados.remove();
	}	
	
	if (valor == '') {
		alert('Campo valor deve ser preenchido!')
	}
	else {
		for (i=0;i<=10;i++){		
		const para = document.createElement("p");
		const node = document.createTextNode(valor+' * '+i+' = '+valor*i);
		para.className = 'valor_tabuada';
		para.appendChild(node);
		document.body.appendChild(para);
		}
	}
}