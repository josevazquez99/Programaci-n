import java.util.Scanner;

/**
 *
 * @author Jose Antonio
 */
public class DecimalABinario {
	public static Scanner teclado = new Scanner(System.in);

	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		System.out.println("Ingrese un número en el sistema decimal positivo");
		double numero = teclado.nextInt();
		String binario = "";
		if (numero > 0) {
			while (numero > 0) {
				if (numero % 2 == 0) {
					binario = "0" + binario;
				} else {
					binario = "1" + binario;
				}
				numero = (int) numero / 2;
			}
		} else if (numero == 0) {
			binario = "0";
		} else {
			binario = "No se pudo convertir el numero. Ingrese solo números positivos";
		}
		System.out.println("El número convertido a binario es: " + binario);
	}
}