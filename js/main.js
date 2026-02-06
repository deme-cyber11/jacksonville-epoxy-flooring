/**
 * Rank & Rent Template - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {

    // ========================================
    // Header Scroll Effect
    // ========================================
    const header = document.querySelector('header');

    function handleScroll() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check

    // ========================================
    // Mobile Menu
    // ========================================
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const mobileMenuClose = document.querySelector('.mobile-menu-close');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.add('active');
            document.body.style.overflow = 'hidden';
        });

        mobileMenuClose.addEventListener('click', () => {
            mobileMenu.classList.remove('active');
            document.body.style.overflow = '';
        });

        // Close on link click
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Close on outside click
        mobileMenu.addEventListener('click', (e) => {
            if (e.target === mobileMenu) {
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // ========================================
    // SPA Navigation
    // ========================================
    function showPage(pageId) {
        // Hide all pages
        document.querySelectorAll('.page-container').forEach(page => {
            page.classList.remove('active');
        });

        // Show target page
        const targetPage = document.getElementById('page-' + pageId);
        if (targetPage) {
            targetPage.classList.add('active');

            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });

            // Update URL hash
            history.pushState(null, '', '#' + pageId);

            // Update header style based on page
            if (pageId === 'home') {
                header.classList.remove('scrolled');
            } else {
                header.classList.add('scrolled');
            }
        }
    }

    // Handle navigation clicks
    document.querySelectorAll('[data-page]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const pageId = this.getAttribute('data-page');
            showPage(pageId);
        });
    });

    // Handle initial hash or direct URL access
    function handleHash() {
        const hash = window.location.hash.slice(1) || 'home';
        showPage(hash);
    }

    handleHash();
    window.addEventListener('hashchange', handleHash);

    // ========================================
    // FAQ Accordion
    // ========================================
    document.querySelectorAll('.faq-question').forEach(question => {
        question.addEventListener('click', function() {
            const faqItem = this.parentElement;
            const isActive = faqItem.classList.contains('active');

            // Close all other FAQs
            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('active');
            });

            // Toggle current
            if (!isActive) {
                faqItem.classList.add('active');
            }
        });
    });

    // ========================================
    // Contact Form
    // ========================================
    const contactForm = document.getElementById('contact-form');
    const formSuccess = document.getElementById('form-success');

    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="ph ph-spinner"></i> Sending...';
            submitBtn.disabled = true;

            try {
                const formData = new FormData(this);
                const response = await fetch(this.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });

                if (response.ok) {
                    contactForm.style.display = 'none';
                    formSuccess.style.display = 'block';
                } else {
                    throw new Error('Form submission failed');
                }
            } catch (error) {
                alert('There was an error sending your message. Please try calling us directly.');
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }
        });
    }

    // Check for success redirect
    if (window.location.hash === '#contact-success') {
        showPage('contact');
        if (contactForm) contactForm.style.display = 'none';
        if (formSuccess) formSuccess.style.display = 'block';
    }

    // ========================================
    // Smooth scroll for anchor links
    // ========================================
    document.querySelectorAll('a[href^="#"]:not([data-page])').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.length > 1) {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // ========================================
    // Form validation visual feedback
    // ========================================
    document.querySelectorAll('.form-group input, .form-group textarea').forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value.trim()) {
                this.classList.add('has-value');
            } else {
                this.classList.remove('has-value');
            }
        });
    });

    // ========================================
    // Scroll Animations (Intersection Observer)
    // ========================================
    const animateOnScrollElements = document.querySelectorAll('.service-card, .trust-card, .testimonial-card, .before-after-card, .process-step, .portfolio-item');

    animateOnScrollElements.forEach((el, index) => {
        el.classList.add('animate-on-scroll');
        el.classList.add('delay-' + ((index % 4) + 1));
    });

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                scrollObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        scrollObserver.observe(el);
    });

    // ========================================
    // Counter Animation for Trust Numbers
    // ========================================
    const counterElements = document.querySelectorAll('.trust-number');
    let countersAnimated = false;

    function animateCounters() {
        if (countersAnimated) return;

        counterElements.forEach(counter => {
            const text = counter.textContent;
            const match = text.match(/^([\d.]+)/);
            if (!match) return;

            const target = parseFloat(match[1]);
            const suffix = text.replace(match[1], '');
            const duration = 2000;
            const steps = 60;
            const increment = target / steps;
            let current = 0;
            const isDecimal = target % 1 !== 0;

            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                counter.innerHTML = (isDecimal ? current.toFixed(1) : Math.floor(current)) + suffix;
            }, duration / steps);
        });

        countersAnimated = true;
    }

    // Observe trust section for counter animation
    const trustSection = document.querySelector('.why-choose-us');
    if (trustSection) {
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounters();
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });

        counterObserver.observe(trustSection);
    }

    // ========================================
    // Sticky CTA Button
    // ========================================
    // Create sticky CTA element
    const stickyCTA = document.createElement('div');
    stickyCTA.className = 'sticky-cta';
    stickyCTA.innerHTML = `
        <a href="tel:+19045550199" class="sticky-cta-btn">
            <i class="ph ph-phone"></i>
            <span>Call Now</span>
        </a>
    `;
    document.body.appendChild(stickyCTA);

    // Show/hide sticky CTA based on scroll
    const hero = document.querySelector('.hero');
    const heroHeight = hero ? hero.offsetHeight : 600;

    function handleStickyCTA() {
        if (window.scrollY > heroHeight * 0.8) {
            stickyCTA.classList.add('visible');
        } else {
            stickyCTA.classList.remove('visible');
        }
    }

    window.addEventListener('scroll', handleStickyCTA);
    handleStickyCTA();

    // ========================================
    // Subtle Parallax on Hero Background
    // ========================================
    const heroBackground = document.querySelector('.hero-background');

    if (heroBackground && window.innerWidth > 768) {
        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY;
            if (scrolled < heroHeight) {
                heroBackground.style.transform = `translateY(${scrolled * 0.3}px)`;
            }
        });
    }

    // ========================================
    // Card Tilt Effect (Desktop only)
    // ========================================
    if (window.innerWidth > 1024) {
        const tiltCards = document.querySelectorAll('.service-card, .trust-card');

        tiltCards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const rotateX = (y - centerY) / 20;
                const rotateY = (centerX - x) / 20;

                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
            });
        });
    }

    // ========================================
    // Before/After Comparison Slider
    // ========================================
    function initBeforeAfterSliders() {
        const sliders = document.querySelectorAll('.comparison-slider, .ba-handle');

        sliders.forEach(slider => {
            const container = slider.closest('.hero-comparison') || slider.closest('.ba-slider');
            if (!container) return;

            const beforeImage = container.querySelector('.comparison-before, .ba-before');
            const handle = slider;

            let isDragging = false;

            function updateSliderPosition(clientX) {
                const rect = container.getBoundingClientRect();
                let position = ((clientX - rect.left) / rect.width) * 100;

                // Clamp position between 5% and 95%
                position = Math.max(5, Math.min(95, position));

                // Update slider handle position
                handle.style.left = `${position}%`;

                // Update before image clip
                if (beforeImage) {
                    beforeImage.style.clipPath = `inset(0 ${100 - position}% 0 0)`;
                }
            }

            // Mouse events
            handle.addEventListener('mousedown', (e) => {
                isDragging = true;
                handle.classList.add('dragging');
                e.preventDefault();
            });

            document.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                updateSliderPosition(e.clientX);
            });

            document.addEventListener('mouseup', () => {
                isDragging = false;
                handle.classList.remove('dragging');
            });

            // Touch events for mobile
            handle.addEventListener('touchstart', () => {
                isDragging = true;
                handle.classList.add('dragging');
            });

            document.addEventListener('touchmove', (e) => {
                if (!isDragging) return;
                updateSliderPosition(e.touches[0].clientX);
            });

            document.addEventListener('touchend', () => {
                isDragging = false;
                handle.classList.remove('dragging');
            });

            // Click on container to move slider
            container.addEventListener('click', (e) => {
                if (e.target === handle || e.target.closest('.comparison-slider, .ba-slider')) return;
                updateSliderPosition(e.clientX);
            });

            // Initialize at 50%
            const rect = container.getBoundingClientRect();
            updateSliderPosition(rect.left + rect.width / 2);
        });
    }

    // Initialize sliders on page load
    initBeforeAfterSliders();

    // Re-initialize on hash change (for SPA navigation)
    window.addEventListener('hashchange', () => {
        setTimeout(initBeforeAfterSliders, 100);
    });

    // ========================================
    // Scroll-triggered Section Animations
    // ========================================
    const sections = document.querySelectorAll('section');

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('section-visible');
            }
        });
    }, { threshold: 0.1 });

    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    // ========================================
    // Portfolio Item Hover Effects
    // ========================================
    const portfolioItems = document.querySelectorAll('.portfolio-item');

    portfolioItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            item.querySelector('.portfolio-overlay')?.classList.add('active');
        });

        item.addEventListener('mouseleave', () => {
            item.querySelector('.portfolio-overlay')?.classList.remove('active');
        });
    });

});
