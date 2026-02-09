import { useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight, Mail, Check } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const NewsletterCTASection = () => {
  const sectionRef = useRef<HTMLElement>(null);
  const leftPanelRef = useRef<HTMLDivElement>(null);
  const rightPanelRef = useRef<HTMLDivElement>(null);

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
        },
      });

      // ENTRANCE (0%-30%)
      scrollTl.fromTo(
        leftPanelRef.current,
        { x: '-45vw', opacity: 0 },
        { x: 0, opacity: 1, ease: 'none' },
        0
      );

      scrollTl.fromTo(
        rightPanelRef.current,
        { x: '65vw' },
        { x: 0, ease: 'none' },
        0
      );

      // SETTLE (30%-70%): Hold

      // EXIT (70%-100%)
      scrollTl.fromTo(
        leftPanelRef.current,
        { x: 0, opacity: 1 },
        { x: '-10vw', opacity: 0, ease: 'power2.in' },
        0.7
      );

      scrollTl.fromTo(
        rightPanelRef.current,
        { x: 0, opacity: 1 },
        { x: '14vw', opacity: 0.35, ease: 'power2.in' },
        0.7
      );
    }, section);

    return () => ctx.revert();
  }, []);

  const benefits = [
    'Weekly policy updates',
    'New material alerts',
    'Market move analysis',
  ];

  return (
    <section
      ref={sectionRef}
      id="newsletter"
      className="section-pinned bg-[#F6F8F6] z-[90]"
    >
      {/* Left text panel */}
      <div
        ref={leftPanelRef}
        className="absolute left-0 top-0 w-full lg:w-[45vw] h-full bg-[#F6F8F6] flex flex-col justify-center px-8 lg:px-[8vw]"
      >
        <div className="flex items-center gap-2 mb-4">
          <Mail size={18} className="text-accent" />
          <span className="micro-label">Newsletter</span>
        </div>

        <h2 className="headline-lg text-3xl sm:text-4xl lg:text-[clamp(34px,3.6vw,56px)] text-primary-dark mb-6">
          Get the week in bioplastics.
        </h2>

        <p className="body-text text-base text-secondary-muted mb-6 max-w-[32vw]">
          A Friday briefing on policy shifts, new materials, and market moves.
        </p>

        {/* Benefits */}
        <div className="space-y-2 mb-8">
          {benefits.map((benefit) => (
            <div key={benefit} className="flex items-center gap-2">
              <Check size={16} className="text-accent" />
              <span className="text-sm text-primary-dark">{benefit}</span>
            </div>
          ))}
        </div>

        <a
          href="#subscribe"
          className="btn-primary inline-flex items-center gap-2 w-fit"
        >
          Subscribe free
          <ArrowRight size={18} />
        </a>

        <p className="text-xs text-secondary-muted mt-4">
          No spam. Unsubscribe anytime.
        </p>
      </div>

      {/* Right media panel */}
      <div
        ref={rightPanelRef}
        className="absolute right-0 top-0 w-full lg:w-[55vw] h-full"
      >
        <div className="relative w-full h-full image-grade">
          <img
            src="/newsletter_field_portrait.jpg"
            alt="Person in field"
            className="w-full h-full object-cover"
          />
        </div>
      </div>
    </section>
  );
};

export default NewsletterCTASection;
