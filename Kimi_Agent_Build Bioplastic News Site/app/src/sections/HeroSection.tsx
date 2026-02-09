import { useEffect, useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const HeroSection = () => {
  const sectionRef = useRef<HTMLElement>(null);
  const leftPanelRef = useRef<HTMLDivElement>(null);
  const rightPanelRef = useRef<HTMLDivElement>(null);
  const headlineRef = useRef<HTMLHeadingElement>(null);
  const subheadlineRef = useRef<HTMLParagraphElement>(null);
  const ctaRowRef = useRef<HTMLDivElement>(null);
  const microStripRef = useRef<HTMLDivElement>(null);

  // Auto-play entrance animation on load
  useEffect(() => {
    const ctx = gsap.context(() => {
      const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

      // Left panel slides in
      tl.fromTo(
        leftPanelRef.current,
        { x: '-60vw' },
        { x: 0, duration: 0.9 }
      );

      // Right panel content staggered
      tl.fromTo(
        headlineRef.current,
        { x: '10vw', opacity: 0 },
        { x: 0, opacity: 1, duration: 0.7 },
        '-=0.5'
      );

      tl.fromTo(
        subheadlineRef.current,
        { x: '10vw', opacity: 0 },
        { x: 0, opacity: 1, duration: 0.7 },
        '-=0.55'
      );

      tl.fromTo(
        ctaRowRef.current,
        { x: '10vw', opacity: 0 },
        { x: 0, opacity: 1, duration: 0.7 },
        '-=0.55'
      );

      tl.fromTo(
        microStripRef.current,
        { y: 24, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.6 },
        '-=0.4'
      );
    }, sectionRef);

    return () => ctx.revert();
  }, []);

  // Scroll-driven exit animation
  useLayoutEffect(() => {
    const section = sectionRef.current;
    if (!section) return;

    const ctx = gsap.context(() => {
      const scrollTl = gsap.timeline({
        scrollTrigger: {
          trigger: section,
          start: 'top top',
          end: '+=130%',
          pin: true,
          scrub: 0.6,
          onLeaveBack: () => {
            // Reset all elements to visible when scrolling back to top
            gsap.set([headlineRef.current, subheadlineRef.current, ctaRowRef.current], {
              x: 0,
              opacity: 1,
            });
            gsap.set(rightPanelRef.current, { x: 0, opacity: 1 });
            gsap.set(leftPanelRef.current, { scale: 1, opacity: 1 });
          },
        },
      });

      // ENTRANCE (0%-30%): Hold - already visible from load animation
      // SETTLE (30%-70%): Hold

      // EXIT (70%-100%)
      scrollTl.fromTo(
        headlineRef.current,
        { x: 0, opacity: 1 },
        { x: '-12vw', opacity: 0, ease: 'power2.in' },
        0.7
      );

      scrollTl.fromTo(
        subheadlineRef.current,
        { x: 0, opacity: 1 },
        { x: '-12vw', opacity: 0, ease: 'power2.in' },
        0.72
      );

      scrollTl.fromTo(
        ctaRowRef.current,
        { x: 0, opacity: 1 },
        { x: '-12vw', opacity: 0, ease: 'power2.in' },
        0.74
      );

      scrollTl.fromTo(
        rightPanelRef.current,
        { x: 0, opacity: 1 },
        { x: '10vw', opacity: 0.35, ease: 'power2.in' },
        0.7
      );

      scrollTl.fromTo(
        leftPanelRef.current,
        { scale: 1, opacity: 1 },
        { scale: 1.03, opacity: 0.5, ease: 'power2.in' },
        0.7
      );
    }, section);

    return () => ctx.revert();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="hero"
      className="section-pinned bg-[#F6F8F6] z-10"
    >
      {/* Left media panel */}
      <div
        ref={leftPanelRef}
        className="absolute left-0 top-0 w-full lg:w-[56vw] h-full"
      >
        <div className="relative w-full h-full image-grade">
          <img
            src="/hero_field_hands.jpg"
            alt="Hands holding a plant in a field"
            className="w-full h-full object-cover"
          />
        </div>
      </div>

      {/* Vertical rule (desktop only) */}
      <div className="hidden lg:block absolute left-[56vw] top-0 w-px h-full bg-[#111C1A]/10" />

      {/* Right content panel */}
      <div
        ref={rightPanelRef}
        className="absolute right-0 top-0 w-full lg:w-[44vw] h-full bg-[#F6F8F6] flex flex-col justify-center px-8 lg:px-[6vw]"
      >
        <div className="max-w-[32vw]">
          <h1
            ref={headlineRef}
            className="headline-xl text-4xl sm:text-5xl lg:text-[clamp(44px,5vw,76px)] text-primary-dark mb-6"
          >
            Sustainable materials. Smarter industry.
          </h1>

          <p
            ref={subheadlineRef}
            className="body-text text-base lg:text-lg text-secondary-muted mb-8 max-w-[30vw]"
          >
            News, market data, and company profiles for the bioplastics
            transition.
          </p>

          <div ref={ctaRowRef} className="flex flex-wrap gap-4 mb-12">
            <a href="#news" className="btn-primary flex items-center gap-2">
              Start reading
              <ArrowRight size={18} />
            </a>
            <a href="#subscribe" className="btn-secondary">
              Get the newsletter
            </a>
          </div>

          <div
            ref={microStripRef}
            className="flex items-center gap-2 text-sm text-secondary-muted hover:text-accent transition-colors cursor-pointer"
          >
            <span className="micro-label">Latest:</span>
            <span>EU packaging rules update</span>
            <ArrowRight size={14} />
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
