import { useState, useEffect } from 'react';
import { Menu, X } from 'lucide-react';

const Navigation = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 100);
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { label: 'News', href: '#news' },
    { label: 'Companies', href: '#companies' },
    { label: 'Events', href: '#events' },
    { label: 'Studies', href: '#studies' },
    { label: 'Glossary', href: '#glossary' },
  ];

  return (
    <>
      <nav
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${
          isScrolled
            ? 'bg-[#F6F8F6]/90 backdrop-blur-md shadow-sm'
            : 'bg-transparent'
        }`}
      >
        <div className="flex items-center justify-between px-6 lg:px-12 py-4">
          {/* Logo */}
          <a
            href="#"
            className="font-heading text-lg font-medium text-primary-dark tracking-tight"
          >
            BioPlastics Today
          </a>

          {/* Desktop Navigation */}
          <div className="hidden lg:flex items-center gap-8">
            {navLinks.map((link) => (
              <a
                key={link.label}
                href={link.href}
                className="text-sm text-primary-dark/80 hover:text-accent transition-colors duration-300"
              >
                {link.label}
              </a>
            ))}
            <a
              href="#subscribe"
              className="btn-primary text-sm"
            >
              Subscribe
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button
            className="lg:hidden p-2 text-primary-dark"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            aria-label="Toggle menu"
          >
            {isMobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </nav>

      {/* Mobile Menu */}
      <div
        className={`fixed inset-0 z-40 bg-[#F6F8F6] transition-transform duration-500 lg:hidden ${
          isMobileMenuOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <div className="flex flex-col items-center justify-center h-full gap-8">
          {navLinks.map((link) => (
            <a
              key={link.label}
              href={link.href}
              className="text-2xl font-heading font-light text-primary-dark hover:text-accent transition-colors"
              onClick={() => setIsMobileMenuOpen(false)}
            >
              {link.label}
            </a>
          ))}
          <a
            href="#subscribe"
            className="btn-primary mt-4"
            onClick={() => setIsMobileMenuOpen(false)}
          >
            Subscribe
          </a>
        </div>
      </div>
    </>
  );
};

export default Navigation;
