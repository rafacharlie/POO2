/**
 * 2. Crea la clase Vehiculo , así como las clases Bicicleta y Coche
 *    como subclases de la primera. Para la clase Vehiculo , crea los
 *    atributos de clase vehiculosCreados y kilometrosTotales , así como
 *    el atributo de instancia kilometrosRecorridos . Crea también algún
 *    método específico para cada una de las subclases. Prueba las
 *    clases creadas mediante un programa con un menú como el que se
 *    muestra a continuación:
 *    
 *    VEHÍCULOS
 *    =========
 *    1. Anda con la bicicleta
 *    2. Haz el caballito con la bicicleta
 *    3. Anda con el coche
 *    4. Quema rueda con el coche
 *    5. Ver kilometraje de la bicicleta
 *    6. Ver kilometraje del coche
 *    7. Ver kilometraje total
 *    8. Salir
 *    Elige una opción (1-8):
 * 
 * @author Rafael Infante
 */
package programasPoo;

import java.util.Scanner;

public class PruebaVehiculos {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// variables
		int opcion = 0;
		int km;

		// instancias
		Bicicleta miBicicleta = new Bicicleta(9);
		Coche miCoche = new Coche(1900);

		// programa
		do {
			System.out.println();
			mostrarMenu(); // muestro el menu
			opcion = sc.nextInt();
			switch (opcion) {
			case 1:
				System.out.print("¿Cuántos kilómetros quiere recorrer en bici? ");
				km = sc.nextInt();
				miBicicleta.recorre(km);
				break;
			case 2:
				miBicicleta.hazCaballito();
				break;
			case 3:
				System.out.print("¿Cuántos kilómetros quiere recorrer en coche? ");
				km = sc.nextInt();
				miCoche.recorre(km);
				break;
			case 4:
				miCoche.quemaRueda();
				break;
			case 5:
				System.out.print("La bicicleta lleva recorridos ");
				System.out.println(miBicicleta.getKilometrosRecorridos() + " Km");
				break;
			case 6:
				System.out.print("El coche lleva recorridos ");
				System.out.println(miCoche.getKilometrosRecorridos() + " Km");
				break;
			case 7:
				System.out.print("Los vehículos llevan recorridos ");
				System.out.println(Vehiculo.getKilometrosTotales() + " Km");
			default:

			}
		} while (opcion != 8);

	}// main

	/**
	 * Funcion vacia que muestra un menu
	 */
	public static void mostrarMenu() {
		System.out.println("\t\tMENU");
		System.out.println("\t\t====\n");
		System.out.println("1. Anda con la bicicleta");
		System.out.println("2. Haz el caballito con la bicicleta");
		System.out.println("3. Anda con el coche");
		System.out.println("4. Quema rueda con el coche");
		System.out.println("5. Ver kilometraje de la bicicleta");
		System.out.println("6. Ver kilometraje del coche");
		System.out.println("7. Ver kilometraje total");
		System.out.println("8. Salir");
		System.out.println("Elige una opción (1-8): ");
	}
}// clase PruebaVehiculo
