package br.com.fiap.bean;

import java.io.*;

public class Pessoa {

    private String codigo;
    private String nome;
    private String email;

    // Métodos construtores

    public Pessoa() {

    }

    public Pessoa(String codigo, String nome, String email) {
        this.codigo = codigo;
        this.nome = nome;
        this.email = email;
    }

    // Métodos Getters and Setters

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    // Métodos da Classe

    public Pessoa ler(String path) throws IOException { // Assinatura do metodo
        BufferedReader br = new BufferedReader(
                new FileReader(path+"/"+codigo+".txt")
        );

        codigo = br.readLine();
        nome = br.readLine();
        email = br.readLine();

        br.close(); // Fechamento da classe BufferReader

        return this; // Faz o retorno do próprio objeto da Classe.
    }

    public String gravar(String path) {
        try {
            File dir = new File(path);

            if (!dir.exists()) {
                dir.mkdir(); // Make a Directory
            }

            PrintWriter pw = new PrintWriter(path+"/"+codigo+".txt");

            pw.println(codigo);
            pw.println(email);

            pw.flush(); // Flush: Descarregar da memória temporária

            pw.close(); // Fechamento da classe PrintWriter

            return "Arquivo gravado com sucesso!";
        } catch (IOException e) {
            return "Falha ao gravar o arquivo: "+e.getMessage();
        }
    }


}
