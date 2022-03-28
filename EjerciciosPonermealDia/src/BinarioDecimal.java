import java.util.Scanner;

public class BinarioDecimal {
	public static Scanner teclado = new Scanner(System.in);

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		System.out.println("Ingrese un número en el sistema decimal positivo");
		int binario = teclado.nextInt();
		int resto, decimal = 0, i = 0;
		while (binario != 0) {
			resto = binario % 10;
			decimal = decimal + (resto * (int) Math.pow(2, i));
			i++;
			binario = binario / 10;
		}
		System.out.println(decimal);
	}
}
