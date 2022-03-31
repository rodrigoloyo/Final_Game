from game.casting.actor import Actor


class Fruits(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, image, points, debug = False):
        """Constructs a new Brick.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._points = points
        
    def get_image(self):
        return self._image

    def get_body(self):
        return self._body

    def get_points(self):
        """Gets the fruits's points.
        
        Returns:
            A number representing the fruits's points.
        """
        return self._points