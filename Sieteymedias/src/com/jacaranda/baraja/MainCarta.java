package com.jacaranda.baraja;

import java.util.Scanner;

public class MainCarta {
	static Scanner teclado = new Scanner(System.in);

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("1.Baraja Española");
		System.out.println("2.Baraja Inglesa");
		System.out.println("Introduce un numero para seleccionar la baraja");
		int tipoBaraja = Integer.parseInt(teclado.nextLine());
		JuegoGUI juego = new JuegoGUI();

		try {
			Baraja b = new Baraja();
			double jugador1 = 0.0, banca = 0.0;
			char respuesta;
			b.barajar();
			System.out.println(b);
			System.out.println("Jugador 1" + "�Quieres una carta?s/n");
			respuesta = teclado.nextLine().charAt(0);
			while (respuesta != 'n') {
				Carta cartas = b.getSiguiente();
				System.out.println(cartas);
				jugador1 += cartas.getValor();
				System.out.println(jugador1);
				System.out.println("�Quieres una carta?s/n");
				respuesta = teclado.nextLine().charAt(0);
			}
			System.out.println(jugador1);
			b.barajar();
			System.out.println(b);
			System.out.println("Banca" + "�Quieres una carta?s/n");
			respuesta = teclado.nextLine().charAt(0);
			while (respuesta != 'n') {
				b.getSiguiente();
				Carta cartas = b.getSiguiente();
				System.out.println(cartas);
				banca += cartas.getValor();
				System.out.println(banca);
				System.out.println("�Quieres una carta?s/n");
				respuesta = teclado.nextLine().charAt(0);
			}
			System.out.println(banca);
			if (jugador1 > 7.5) {
				System.out.println("gana la banca");
			} else if (banca > 7.5) {
				System.out.println("gana jugador");
			} else if (jugador1 > banca) {
				System.out.println("gana jugador");
			} else if (banca > jugador1) {
				System.out.println("gana la banca");
			} else {
				System.out.println("Empate");
			}
		} catch (CartaException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}