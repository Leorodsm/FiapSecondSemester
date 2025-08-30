package br.com.fiap.main;

import br.com.fiap.bean.Pessoa;

import javax.swing.*;
import java.io.IOException;

public class UsaPessoa {
    public static void main(String[] args) {
        String codigo, nome, email, path;
        int opcao;
        Pessoa pessoa;

        do {
            try {
                opcao = Integer.parseInt(JOptionPane.showInputDialog("Escolha:"))

            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Erro de conversão / formato numérico: "+e.getMessage(),"Erro",JOptionPane.ERROR_MESSAGE);
            } catch (IOException e) {
                JOptionPane.showMessageDialog(null, "Erro ao acessar arquivo: "+e.getMessage(),"Erro",JOptionPane.ERROR_MESSAGE);
            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Erro: "+e.getMessage(),"Erro",JOptionPane.ERROR_MESSAGE);
            }

        } while (JOptionPane.showConfirmDialog(null,"Deseja continuar?","Atenção!",JOptionPane.YES_NO_OPTION,JOptionPane.QUESTION_MESSAGE) == 0);

        JOptionPane.showMessageDialog(null,"Fim de programa.");

    }
}
