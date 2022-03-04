package SieteYmedia;

import java.util.Arrays;

import Sieteymedias.Carta;

public class Barajaespannola {
	private int siguiente;
	private int numCartas = 40;
	private Carta[] cartas = new Carta[numCartas];

	public Barajaespannola(int numCartas, int siguiente) {
		super();
		this.cartas = new Carta[numCartas];
		this.siguiente = 0;
	}

	private String generarPalo() {
		String palo = "";
		int numPalo = claseRandom.nextInt(3);
		if (numPalo == 0) {
			palo = "Espadas";
		}
		if (numPalo == 1) {
			palo = "Oros";
		}
		if (numPalo == 0) {
			palo = "Bastos";
		}
		if (numPalo == 0) {
			palo = "Copas";
		}
		return palo;
	}

	public String toString() {
		String resultado = "";
		for (int i = 0; i < this.numCartas; i++) {
			resultado = resultado + "" + cartas[i];
		}
		return resultado;
	}

}