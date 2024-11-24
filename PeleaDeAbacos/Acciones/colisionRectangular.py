class RectangularCollision3D:
    def __init__(self, x, y, z, width, height, depth):
        """
        Inicializa la caja de colisión 3D con una posición (x, y, z) y dimensiones (width, height, depth).
        
        :param x: Coordenada X de la caja (centro o esquina inferior)
        :param y: Coordenada Y de la caja (centro o esquina inferior)
        :param z: Coordenada Z de la caja (centro o esquina inferior)
        :param width: Ancho de la caja
        :param height: Altura de la caja
        :param depth: Profundidad de la caja
        """
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth

    def get_min_max(self):
        """
        Calcula las coordenadas mínimas y máximas de la caja a partir de la posición y dimensiones.
        
        :return: Una tupla con las coordenadas mínimas y máximas (x_min, y_min, z_min, x_max, y_max, z_max)
        """
        x_min = self.x - self.width / 2
        y_min = self.y - self.height / 2
        z_min = self.z - self.depth / 2
        x_max = self.x + self.width / 2
        y_max = self.y + self.height / 2
        z_max = self.z + self.depth / 2
        return x_min, y_min, z_min, x_max, y_max, z_max

    def check_collision(self, other):
        """
        Verifica si hay colisión entre esta caja 3D y otra.
        
        :param other: Otro objeto RectangularCollision3D con el que verificar la colisión
        :return: True si hay colisión, False en caso contrario
        """
        # Obtener las coordenadas mínimas y máximas de ambas cajas
        x_min1, y_min1, z_min1, x_max1, y_max1, z_max1 = self.get_min_max()
        x_min2, y_min2, z_min2, x_max2, y_max2, z_max2 = other.get_min_max()

        # Verifica si las cajas no se solapan en algún eje
        if x_max1 < x_min2 or x_min1 > x_max2:
            return False  # No hay colisión en el eje X

        if y_max1 < y_min2 or y_min1 > y_max2:
            return False  # No hay colisión en el eje Y

        if z_max1 < z_min2 or z_min1 > z_max2:
            return False  # No hay colisión en el eje Z

        return True  # Si no se cumplen las condiciones anteriores, hay colisión

    def move(self, dx, dy, dz):
        """
        Mueve la caja 3D por la distancia (dx, dy, dz).
        
        :param dx: Desplazamiento en el eje X
        :param dy: Desplazamiento en el eje Y
        :param dz: Desplazamiento en el eje Z
        """
        self.x += dx
        self.y += dy
        self.z += dz

    def set_position(self, x, y, z):
        """
        Establece la posición de la caja 3D.
        
        :param x: Nueva coordenada X
        :param y: Nueva coordenada Y
        :param z: Nueva coordenada Z
        """
        self.x = x
        self.y = y
        self.z = z

    def get_position(self):
        """
        Devuelve la posición de la caja 3D.
        
        :return: Una tupla con la posición (x, y, z)
        """
        return self.x, self.y, self.z

    def get_dimensions(self):
        """
        Devuelve las dimensiones de la caja 3D (width, height, depth).
        
        :return: Una tupla con las dimensiones (width, height, depth)
        """
        return self.width, self.height, self.depth
