<template>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  
    <footer>
      <div class="footer-content">
          <div class="contact-info">
            <h2>Contacto</h2>
            <p>Dirección: 123 Calle del Festival</p>
            <p>Teléfono: (123) 456-7890</p>
            <p>Correo Electrónico: info@festivaldemusica.com</p>
          </div>
          <div class="social-media">
            <h2>Redes Sociales</h2>
            <a href="#" class="icon">Facebook</a>
            <a href="#" class="icon">Twitter</a>
            <a href="#" class="icon">Instagram</a>
          </div>
      </div>
      <div class="copyright">
        <p>&copy; 2023 Festival de Música. Todos los derechos reservados.</p>
      </div>
    </footer>
      
  </template>
  
  <script>
  export default {
  
  }
  </script>
  
  
  <style>
  
  footer{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center; 
      font-family: 'Manrope', sans-serif;
      font-size: small;
  }
  
  .footer-content{
      display: flex;
      flex-direction: row;
  }
  
  .social-media, .contact-info{
      display: flex;
      flex-direction: column;
      text-align: center;
      padding: 5vw;
  }
  
  .contact-info p{
      margin: 0;
  }
  
  .icon{
    text-decoration: none;
    color: black;
  }
  
  </style>