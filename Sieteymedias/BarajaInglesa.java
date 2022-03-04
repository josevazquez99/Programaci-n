package SieteYmedia;

import java.util.Arrays;
import java.util.Objects;

import Sieteymedias.Carta;

public class BarajaInglesa {
	private int siguiente;
	private int numCartas = 40;
	private Carta[] cartas = new Carta[numCartas];

	public BarajaInglesa(int numCartas, int siguiente) {
		super();
		this.cartas = new Carta[numCartas];
		this.siguiente = 0;
	}

	private String generarPalo() {
		String palo = "";
		int numPalo = claseRandom.nextInt(3);
		if (numPalo == 0) {
			palo = "Picas";
		}
		if (numPalo == 1) {
			palo = "Rombos";
		}
		if (numPalo == 0) {
			palo = "Treboles";
		}
		if (numPalo == 0) {
			palo = "Corazones";
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