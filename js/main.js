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

});
