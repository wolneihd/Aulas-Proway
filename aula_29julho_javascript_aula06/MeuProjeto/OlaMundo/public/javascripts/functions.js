function enviar() {
    var nome = $('#nome').val();
    var idade = parseInt($('#idade').val());
    console.log(`${nome} | ${idade}`);
    $('.resultado').text(`Seu nome é ${nome}, idade: ${idade}`);
}

// pokedex:
function gerarPokedex() {
    var nova_img = '';
    var pokemon = $('.pokemon');
    for (i = 0; i < 150; i++) {
        nova_img += `<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${i}.png">`;
    }
    pokemon.html(nova_img);
}

//gerarPokedex()

async function buscarPokemon() {
    var nome = $('#nome').val();
    var pokemon = $('.pokemon');
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${nome}`);
    if (!response.ok) {
        throw new error("Could not fetch resource!");
    }
    const data = await response.json();
    console.log(data);
    //
    pokemon.html(`<img src="${data['sprites']['front_default']}">`);    
    $('#nome-pokemon').html(data['name']);
    $('#numero-pokemon').html(data['id']);
    $('#numero-pokemon').html(`tipo do pokemon: ${data['types'][0]['type']['name']}`);
}