import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Clase para representar un Usuario del cine.
 */
class Usuario {
    String nombre;
    String email;

    public Usuario(String nombre, String email) {
        this.nombre = nombre;
        this.email = email;
    }

    public String getNombre() {
        return nombre;
    }
}

/**
 * Clase para representar una Reserva.
 */
class Reserva {
    String nombreUsuario;
    String pelicula;

    public Reserva(String nombreUsuario, String pelicula) {
        this.nombreUsuario = nombreUsuario;
        this.pelicula = pelicula;
    }
}

/**
 * Clase principal que simula la lógica del Cine.
 */
public class Cine {
    // Atributos de la clase Cine
    public List<Usuario> usuarios = new ArrayList<>();
    public List<String> peliculas = new ArrayList<>(Arrays.asList("Matrix", "Inception", "Interstellar"));
    public List<Reserva> reservas = new ArrayList<>();

    /**
     * Registra un nuevo usuario en la lista.
     * @param nombre El nombre del usuario.
     * @param email El correo electrónico del usuario.
     */
    public void registrarUsuario(String nombre, String email) {
        this.usuarios.add(new Usuario(nombre, email));
        System.out.println("Usuario " + nombre + " registrado.");
    }

    /**
     * Muestra todas las películas disponibles en la cartelera.
     */
    public void mostrarCartelera() {
        System.out.println("\n--- Cartelera ---");
        for (String p : this.peliculas) {
            System.out.println(p);
        }
        System.out.println("-----------------\n");
    }

    /**
     * Realiza una reserva para un usuario y una película.
     * @param nombreUsuario El nombre del usuario que hace la reserva.
     * @param pelicula El nombre de la película a reservar.
     */
    public void reservar(String nombreUsuario, String pelicula) {
        boolean usuarioEncontrado = false;
        // Busca si el usuario está registrado
        for (Usuario u : this.usuarios) {
            if (u.getNombre().equals(nombreUsuario)) {
                usuarioEncontrado = true;
                break;
            }
        }

        if (!usuarioEncontrado) {
            System.out.println("Usuario no registrado");
            return;
        }

        // Verifica si la película está en la lista
        if (this.peliculas.contains(pelicula)) {
            this.reservas.add(new Reserva(nombreUsuario, pelicula));
            System.out.println("Reserva exitosa para " + nombreUsuario + " - Película: " + pelicula);
        } else {
            System.out.println("Película no disponible");
        }
    }

    /**
     * Valida si un email contiene el carácter '@'.
     * @param email El email a validar.
     * @return true si es válido, false en caso contrario.
     */
    public boolean duplicarValidacionEmail(String email) {
        return email.contains("@");
    }

    /**
     * Segunda validación de email (idéntica a la primera).
     * @param email El email a validar.
     * @return true si es válido, false en caso contrario.
     */
    public boolean duplicarValidacionEmail2(String email) {
        return email.contains("@");
    }

    /**
     * Método principal para ejecutar el programa.
     */
    public static void main(String[] args) {
        Cine c = new Cine();
        c.registrarUsuario("Pedro", "pedro@mail.com");
        c.mostrarCartelera();
        c.reservar("Pedro", "Matrix");
    }
}