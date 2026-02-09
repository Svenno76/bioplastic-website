import { useState, useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight, Linkedin, Rss, Mail, MapPin, Phone } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const SubscribeFooterSection = () => {
  const sectionRef = useRef<HTMLElement>(null);
  const leftColumnRef = useRef<HTMLDivElement>(null);
  const rightImageRef = useRef<HTMLDivElement>(null);
  const [email, setEmail] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  useLayoutEffect(() => {
    const section = sectionRef.current;
    if (!section) return;

    const ctx = gsap.context(() => {
      // Left column animation
      gsap.fromTo(
        leftColumnRef.current,
        { y: 30, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 0.6,
          scrollTrigger: {
            trigger: leftColumnRef.current,
            start: 'top 75%',
            toggleActions: 'play none none reverse',
          },
        }
      );

      // Right image animation
      gsap.fromTo(
        rightImageRef.current,
        { x: '6vw', scale: 1.04, opacity: 0 },
        {
          x: 0,
          scale: 1,
          opacity: 1,
          duration: 0.7,
          scrollTrigger: {
            trigger: rightImageRef.current,
            start: 'top 75%',
            toggleActions: 'play none none reverse',
          },
        }
      );

      // Parallax effect on image
      gsap.to(rightImageRef.current, {
        y: -12,
        scrollTrigger: {
          trigger: section,
          start: 'top bottom',
          end: 'bottom top',
          scrub: 0.4,
        },
      });
    }, section);

    return () => ctx.revert();
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (email) {
      setIsSubmitted(true);
      setTimeout(() => {
        setEmail('');
        setIsSubmitted(false);
      }, 3000);
    }
  };

  const footerLinks = [
    { label: 'About', href: '#' },
    { label: 'Contact', href: '#' },
    { label: 'Privacy', href: '#' },
    { label: 'Terms', href: '#' },
  ];

  return (
    <section
      ref={sectionRef}
      id="subscribe"
      className="relative bg-[#0B1E1C] z-[100]"
    >
      {/* Main content area */}
      <div className="flex flex-col lg:flex-row">
        {/* Left column - Form */}
        <div
          ref={leftColumnRef}
          className="w-full lg:w-[45vw] px-8 lg:px-[8vw] py-16 lg:py-24"
        >
          <h2 className="headline-lg text-3xl sm:text-4xl lg:text-[clamp(34px,3.6vw,56px)] text-white mb-4">
            Join the industry read.
          </h2>

          <p className="body-text text-base text-white/70 mb-8 max-w-[32vw]">
            Subscribe for weekly analysis, data drops, and event invites.
          </p>

          {/* Email form */}
          <form onSubmit={handleSubmit} className="mb-12">
            <div className="flex flex-col sm:flex-row gap-3">
              <div className="relative flex-1">
                <Mail
                  size={18}
                  className="absolute left-4 top-1/2 -translate-y-1/2 text-white/50"
                />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Email address"
                  className="w-full pl-12 pr-4 py-3 bg-white/10 border border-white/20 rounded-full text-white placeholder:text-white/50 focus:outline-none focus:border-accent transition-colors"
                  required
                />
              </div>
              <button
                type="submit"
                className="btn-primary flex items-center justify-center gap-2"
                disabled={isSubmitted}
              >
                {isSubmitted ? (
                  <>Subscribed!</>
                ) : (
                  <>
                    Subscribe
                    <ArrowRight size={18} />
                  </>
                )}
              </button>
            </div>
          </form>

          {/* Contact info */}
          <div className="space-y-3 mb-12">
            <div className="flex items-center gap-3 text-white/70">
              <MapPin size={16} />
              <span className="text-sm">Berlin, Germany</span>
            </div>
            <div className="flex items-center gap-3 text-white/70">
              <Phone size={16} />
              <span className="text-sm">+49 30 1234 5678</span>
            </div>
          </div>
        </div>

        {/* Right column - Image */}
        <div
          ref={rightImageRef}
          className="w-full lg:w-[55vw] h-[50vh] lg:h-[70vh] lg:mt-12"
        >
          <div className="relative w-full h-full image-grade">
            <img
              src="/footer_coffee_meeting.jpg"
              alt="Coffee meeting"
              className="w-full h-full object-cover"
            />
          </div>
        </div>
      </div>

      {/* Footer links */}
      <div className="border-t border-white/10 px-8 lg:px-[8vw] py-6">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex flex-wrap items-center justify-center gap-6">
            {footerLinks.map((link) => (
              <a
                key={link.label}
                href={link.href}
                className="text-sm text-white/60 hover:text-white transition-colors"
              >
                {link.label}
              </a>
            ))}
          </div>

          <div className="flex items-center gap-4">
            <a
              href="#"
              className="p-2 text-white/60 hover:text-white hover:bg-white/10 rounded-full transition-colors"
              aria-label="LinkedIn"
            >
              <Linkedin size={20} />
            </a>
            <a
              href="#"
              className="p-2 text-white/60 hover:text-white hover:bg-white/10 rounded-full transition-colors"
              aria-label="RSS Feed"
            >
              <Rss size={20} />
            </a>
          </div>
        </div>

        <div className="mt-6 pt-6 border-t border-white/5 text-center">
          <p className="text-xs text-white/40">
            © 2025 BioPlastics Today. All rights reserved.
          </p>
        </div>
      </div>
    </section>
  );
};

export default SubscribeFooterSection;
