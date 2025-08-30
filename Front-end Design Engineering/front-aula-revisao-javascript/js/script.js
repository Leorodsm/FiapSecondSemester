let pessoa = {
    nome: "admin",
    senha: "admin",
    email: "admin@example.com",
    idade: 30,
    cidade: "São Paulo",
    estado: "SP",
    pais: "Brasil",
    nomeCompleto: function() {
        return `${this.nome} (${this.email})`;
    }
};
console.log(pessoa.nomeCompleto())