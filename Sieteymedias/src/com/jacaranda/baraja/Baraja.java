package com.jacaranda.baraja;

import java.util.Arrays;

public class Baraja {
	private int numcarta;
	private int siguiente;
	private Carta[] cartas;

	public Baraja() {
		super();
		this.numcarta = 40;
		this.cartas = new Carta[numcarta];
		this.siguiente = 0;
	}

	public Carta[] getCartas() {
		return cartas;
	}

	private String generaPalo() {
		String palos;
		String[] palo = { "Espada", "Oro", "Basto", "Copa" };
		int numeroAleatorio = (int) (Math.random() * 3);
		palos = palo[numeroAleatorio];
		return palos;

	}

	private int generaNumero() {
		int numero = (int) (Math.random() * 10 + 1);
		return numero;
	}

	public void barajar() throws CartaException {
		int indiceCarta = 0;
		boolean encontrado = false;
		while (indiceCarta < numcarta) {
			Carta c = new Carta(generaNumero(), generaPalo());
			for (int j = 0; j <= indiceCarta && encontrado == true; j++) {
				if (cartas[j].equals(c)) {
					encontrado = true;
				}
			}
			if (encontrado == false) {
				cartas[indiceCarta++] = c;
			}
		}

	}

	public Carta getSiguiente() throws CartaException {
		int i = 0;
		Carta resultado = new Carta(generaNumero(), generaPalo());
		i++;
		return resultado;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + Arrays.hashCode(cartas);
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Baraja other = (Baraja) obj;
		return Arrays.equals(cartas, other.cartas);
	}

	@Override
	public String toString() {
		return "Baraja [numcarta=" + numcarta + ", siguiente=" + siguiente + ", cartas=" + Arrays.toString(cartas)
				+ "]";
	}

}


