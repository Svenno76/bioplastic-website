import { useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight, BookOpen } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const GlossarySection = () => {
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
        { x: '-70vw' },
        { x: 0, ease: 'none' },
        0
      );

      scrollTl.fromTo(
        rightPanelRef.current,
        { x: '45vw', opacity: 0 },
        { x: 0, opacity: 1, ease: 'none' },
        0
      );

      // SETTLE (30%-70%): Hold

      // EXIT (70%-100%)
      scrollTl.fromTo(
        leftPanelRef.current,
        { x: 0, opacity: 1 },
        { x: '-16vw', opacity: 0, ease: 'power2.in' },
        0.7
      );

      scrollTl.fromTo(
        rightPanelRef.current,
        { x: 0, opacity: 1 },
        { x: '10vw', opacity: 0, ease: 'power2.in' },
        0.7
      );
    }, section);

    return () => ctx.revert();
  }, []);

  const glossaryTerms = [
    'Biodegradation',
    'Drop-in resins',
    'PLA',
    'PHA',
    'Bio-PE',
    'Compostable',
  ];

  return (
    <section
      ref={sectionRef}
      id="glossary"
      className="section-pinned bg-[#F6F8F6] z-50"
    >
      {/* Left media panel */}
      <div
        ref={leftPanelRef}
        className="absolute left-0 top-0 w-full lg:w-[60vw] h-full"
      >
        <div className="relative w-full h-full image-grade">
          <img
            src="/glossary_leaves_sky.jpg"
            alt="Leaves against sky"
            className="w-full h-full object-cover"
          />
        </div>
      </div>

      {/* Right text panel */}
      <div
        ref={rightPanelRef}
        className="absolute right-0 top-0 w-full lg:w-[40vw] h-full bg-[#F6F8F6] flex flex-col justify-center px-8 lg:px-[5vw]"
      >
        <div className="flex items-center gap-2 mb-4">
          <BookOpen size={20} className="text-accent" />
          <span className="micro-label">Knowledge Base</span>
        </div>

        <h2 className="headline-lg text-3xl sm:text-4xl lg:text-[clamp(34px,3.6vw,56px)] text-primary-dark mb-6">
          Speak the language.
        </h2>

        <p className="body-text text-base text-secondary-muted mb-6 max-w-[28vw]">
          From biodegradation to drop-in resins—clear definitions for a complex
          supply chain.
        </p>

        {/* Term tags */}
        <div className="flex flex-wrap gap-2 mb-8">
          {glossaryTerms.map((term) => (
            <span
              key={term}
              className="px-3 py-1 bg-white border border-[#111C1A]/10 rounded-full text-sm text-primary-dark hover:bg-accent hover:text-white hover:border-accent transition-colors cursor-pointer"
            >
              {term}
            </span>
          ))}
        </div>

        <a
          href="#"
          className="btn-primary inline-flex items-center gap-2 w-fit"
        >
          Open the glossary
          <ArrowRight size={18} />
        </a>
      </div>
    </section>
  );
};

export default GlossarySection;
