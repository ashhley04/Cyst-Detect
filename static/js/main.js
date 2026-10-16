/**
* Template Name: Medilab - v4.7.1
* Template URL: https://bootstrapmade.com/medilab-free-medical-bootstrap-theme/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  let selectTopbar = select('#topbar')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
        if (selectTopbar) {
          selectTopbar.classList.add('topbar-scrolled')
        }
      } else {
        selectHeader.classList.remove('header-scrolled')
        if (selectTopbar) {
          selectTopbar.classList.remove('topbar-scrolled')
        }
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Initiate glightbox 
   */
  document.addEventListener('DOMContentLoaded', (event) => {
    // Initialize GLightbox
    const lightbox = GLightbox({
        selector: '.glightbox'
    });
});

  /**
   * Initiate Gallery Lightbox 
   */
  const galelryLightbox = GLightbox({
    selector: '.galelry-lightbox'
  });

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 2,
        spaceBetween: 20
      }
    }
  });

  "use strict";

  // Existing code from your template (already provided)

  // Add your map initialization and nearby clinic search functionality here
  
  // Function to initialize the map
  function initializeMap(lat, lon) {
      var map = L.map('map').setView([lat, lon], 13);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 18,
      }).addTo(map);

      // Fetch nearby clinics
      searchNearbyClinics(lat, lon, map);
  }

  // Function to search for nearby clinics or scanning centers
  function searchNearbyClinics(lat, lon, map) {
      var overpassUrl = `https://overpass-api.de/api/interpreter?data=[out:json];node[amenity=hospital](around:5000,${lat},${lon});out;`;
      
      fetch(overpassUrl)
        .then(response => response.json())
        .then(data => {
          data.elements.forEach(function (element) {
            var clinicLat = element.lat;
            var clinicLon = element.lon;
            var clinicName = element.tags.name || "Unknown Center";

            // Add markers for each clinic found
            L.marker([clinicLat, clinicLon]).addTo(map)
              .bindPopup(clinicName);
          });
        });
  }

  // Function to get user's location
  function getLocation() {
      if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
              var lat = position.coords.latitude;
              var lon = position.coords.longitude;
              initializeMap(lat, lon);
          });
      } else {
          alert("Geolocation is not supported by this browser.");
      }
  }

  // Call the getLocation function when the page loads
  document.addEventListener('DOMContentLoaded', function() {
      getLocation();
  });

  const socket = io.connect('http://localhost:5017');
const localVideo = document.getElementById('localVideo');
const remoteVideo = document.getElementById('remoteVideo');

let localStream;
let peerConnection;
const servers = null; // STUN/TURN servers configuration
const constraints = {
  video: true,
  audio: true
};

// Request access to the user's webcam and microphone
navigator.mediaDevices.getUserMedia(constraints)
  .then(stream => {
    localStream = stream;
    localVideo.srcObject = stream;
  })
  .catch(error => console.error('Error accessing media devices.', error));

socket.on('offer', (offer) => {
  // Handle incoming offer
  handleOffer(offer);
});

socket.on('answer', (answer) => {
  // Handle incoming answer
  handleAnswer(answer);
});

socket.on('candidate', (candidate) => {
  // Handle incoming ICE candidates
  handleCandidate(candidate);
});

function handleOffer(offer) {
  peerConnection = new RTCPeerConnection(servers);
  peerConnection.onicecandidate = ({ candidate }) => {
    if (candidate) {
      socket.emit('candidate', candidate);
    }
  };

  peerConnection.ontrack = (event) => {
    remoteVideo.srcObject = event.streams[0];
  };

  peerConnection.setRemoteDescription(new RTCSessionDescription(offer))
    .then(() => peerConnection.createAnswer())
    .then(answer => {
      return peerConnection.setLocalDescription(answer);
    })
    .then(() => {
      socket.emit('answer', peerConnection.localDescription);
    })
    .catch(error => console.error('Error handling offer', error));

  localStream.getTracks().forEach(track => {
    peerConnection.addTrack(track, localStream);
  });
}

function handleAnswer(answer) {
  peerConnection.setRemoteDescription(new RTCSessionDescription(answer))
    .catch(error => console.error('Error handling answer', error));
}

function handleCandidate(candidate) {
  peerConnection.addIceCandidate(new RTCIceCandidate(candidate))
    .catch(error => console.error('Error adding ICE candidate', error));
}



})()