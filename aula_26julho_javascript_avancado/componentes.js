function header() {
    return `<h1>Bem-vindo!!</h1>`
}

function form() {
    let form = `
    <h1>Digite os dados pra cadastro!</h1>
    <form>
        <input type="text" name="dsNome" id="dsNome" placeholder="nome">
        <input type="number" name="nrIdade" id="nrIdade" placeholder="idade">
        <input type="email" name="dsMail" id="dsMail" placeholder="E-mail"> 
        <button type="submit" onclick='this.form.action="formAction"'>Enviar</button>
    </form>
    `
    return form
}

module.exports = { header, form }