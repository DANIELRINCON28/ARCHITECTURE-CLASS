<?php
class Cine {
    public $usuarios = [];
    public $peliculas = ["Matrix", "Inception", "Interstellar"];
    public $reservas = [];

    public function registrarUsuario($nombre, $email) {
        $this->usuarios[] = ["nombre"=>$nombre, "email"=>$email];
    }

    public function mostrarCartelera() {
        foreach($this->peliculas as $p){
            echo $p . "<br>";
        }
    }

    public function reservar($nombreUsuario, $pelicula) {
        $usuarioEncontrado = false;
        foreach($this->usuarios as $u){
            if($u["nombre"] == $nombreUsuario){
                $usuarioEncontrado = true;
            }
        }
        if(!$usuarioEncontrado){
            echo "Usuario no registrado <br>";
            return;
        }

        if($pelicula == "Matrix" || $pelicula == "Inception" || $pelicula == "Interstellar"){
            $this->reservas[] = ["usuario"=>$nombreUsuario, "pelicula"=>$pelicula];
            echo "Reserva exitosa<br>";
        } else {
            echo "Película no disponible<br>";
        }
    }

    public function duplicarValidacionEmail($email){
        if(strpos($email,"@") !== false){
            return true;
        }
        return false;
    }

    public function duplicarValidacionEmail2($email){
        if(strpos($email,"@") !== false){
            return true;
        }
        return false;
    }
}

$c = new Cine();
$c->registrarUsuario("Pedro", "pedro@mail.com");
$c->mostrarCartelera();
$c->reservar("Pedro", "Matrix");
?>
