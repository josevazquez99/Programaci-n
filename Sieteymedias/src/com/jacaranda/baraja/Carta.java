package com.jacaranda.baraja;

import java.util.Objects;

public class Carta {
	private int number;
	private String palo;

	public Carta(int number, String palo) throws CartaException {
		super();
		if (number < 1 || number > 10) {
			throw new CartaException(" Error, Esa carta no es correcta");
		}
		this.number = number;
		if (palo != "Espada" && palo != "Oro" && palo != "Basto" && palo != "Copa") {
			throw new CartaException("Error, ese palo no es el adecuado");
		}
		this.palo = palo;
	}

	public int getNumber() {
		return number;
	}

	public String getPalo() {
		return palo;
	}

	public double getValor() {
		double valor;
		if (this.number > 7 && this.number <= 10) {
			valor = 0.5;
		} else {
			valor = this.number;
		}
		return valor;
	}

	@Override
	public int hashCode() {
		return Objects.hash(number, palo);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Carta other = (Carta) obj;
		return number == other.number && Objects.equals(palo, other.palo);
	}

	@Override
	public String toString() {
		String cadenaFinal = "";
		if (this.number == 8) {
			cadenaFinal = "Carta [number=" + "Sota" + ", palo=" + getPalo() + "]";
		} else if (this.number == 9) {
			cadenaFinal = "Carta [number=" + "Caballo" + ", palo=" + getPalo() + "]";
		} else if (this.number == 10) {
			cadenaFinal = "Carta [number=" + "Rey" + ", palo=" + getPalo() + "]";
		} else {
			cadenaFinal = "Carta [number=" + number + ", palo=" + getPalo() + "]";
		}
		return cadenaFinal;
	}

}