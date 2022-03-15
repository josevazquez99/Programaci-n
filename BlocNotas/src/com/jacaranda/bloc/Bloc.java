package com.jacaranda.bloc;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.Objects;

import com.jacaranda.nota.Nota;
import com.jacaranda.nota.NotaAlarma;
import com.jacaranda.nota.NotaAlarmaException;

public class Bloc extends BlocException {

	private static final int NUMERONOTASMAXIMA=3;
	private int numNotas;
	private String nombre;
	private Nota[] nota;
	
	public Bloc(String nombre) throws BlocException{
		super();
		this.nombre = nombre;
		this.numNotas = 0;
		this.nota = new Nota[NUMERONOTASMAXIMA];
	}
	
	public void addNota(String texto) throws BlocException {
		if (numNotas == NUMERONOTASMAXIMA) {
			throw new BlocException("Error");
		}
		nota[numNotas++] = new Nota(texto);
	}
	
	public void addNota(String texto, LocalDateTime fechaAlarma, boolean activado ) throws BlocException {
		if (numNotas == NUMERONOTASMAXIMA) {
			throw new BlocException("Error");
		}
		try {
			nota[numNotas++] = new NotaAlarma(texto, fechaAlarma, activado);
			numNotas++;
		} catch (NotaAlarmaException e) {
			// TODO Auto-generated catch block
			throw new BlocException("Error al crear la nota con alarma");
		}
	}
	
	public void addNota(String texto, LocalDateTime fechaAlarma, int minutosARepetir ) throws BlocException {
		if (numNotas == NUMERONOTASMAXIMA) {
			throw new BlocException("Error");
		}
		try {
			nota[numNotas++] = new NotaAlarma(texto, fechaAlarma, minutosARepetir);
			numNotas++;
		} catch (NotaAlarmaException e) {
			// TODO Auto-generated catch block
			throw new BlocException("Error al crear la nota con alarma");
		}
	}
	
	public String getNota(int numNotas) throws BlocException {
		if (numNotas > this.numNotas || numNotas < 0) {
			throw new BlocException("Nota no existente");
		}
		return nota[numNotas].toString();
	}
	
	public void borrarNota(int posicion) throws BlocException {
		if (posicion >= numNotas) {
			throw new BlocException("Error");
		}
		for (int i = posicion; i < numNotas-1; i++) {
			nota[i] = nota[i+1];
		}
		numNotas--;
	}

	public void updateNota(int pos, String texto) throws BlocException {
		if (numNotas > this.numNotas || numNotas < 0) {
			throw new BlocException("Nota no existente");
		}
		nota[numNotas].setTexto(texto);
	}
	
	public void activa(int pos) throws Exception {
		if (numNotas > this.numNotas || numNotas < 0) {
			throw new BlocException("Nota no existente");
		}
		if (nota[pos] instanceof NotaAlarma) {
			((NotaAlarma) nota[pos]).activar();
		}
		else {
			throw new BlocException("Imposible activar nota");
		}		
	}
	
	public void desactiva(int pos) throws Exception {
		if (numNotas > this.numNotas || numNotas < 0) {
			throw new BlocException("Nota no existente");
		}
		if (nota[pos] instanceof NotaAlarma) {
			((NotaAlarma) nota[pos]).desactivar();
		}
		else {
			throw new BlocException("Imposible desactivar nota");
		}		
	}
	
	public static int getNumeroNotasMaxima() {
		return NUMERONOTASMAXIMA;
	}

	public String getNombre() {
		return nombre;
	}

	@Override
	public int hashCode() {
		return Objects.hash(nombre);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Bloc other = (Bloc) obj;
		return Objects.equals(nombre, other.nombre);
	}

	@Override
	public String toString() {
		StringBuilder result = new StringBuilder("Nombre del bloc" + nombre + "\n");
		for (int i=0; i<numNotas; i++) {
			result.append(nota[i].toString()+"\n");
		}
		return result.toString();
	}
	
	public String ordenaBloc() {
		Nota[] blocOrdenado = new Nota [numNotas];
		StringBuilder result = new StringBuilder("Array ordenado");
		for (int i = 0; i < this.numNotas;i++) {
			blocOrdenado[i] = nota[i];
		}
		Arrays.sort(blocOrdenado);
		for (int i = 0; i < this.numNotas;i++) {
			result.append(blocOrdenado[i]);
		}
		return result.toString();
	}
}
