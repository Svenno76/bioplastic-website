import { useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight, Sparkles, Beaker, Award } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const InnovationSpotlightSection = () => {
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
        { x: '-65vw' },
        { x: 0, ease: 'none' },
        0
      );

      scrollTl.fromTo(
        rightPanelRef.current,
        { x: '50vw', opacity: 0 },
        { x: 0, opacity: 1, ease: 'none' },
        0
      );

      // SETTLE (30%-70%): Hold (slightly later settle at 0.52)

      // EXIT (70%-100%)
      scrollTl.fromTo(
        leftPanelRef.current,
        { x: 0, opacity: 1 },
        { x: '-14vw', opacity: 0, ease: 'power2.in' },
        0.7
      );

      scrollTl.fromTo(
        rightPanelRef.current,
        { x: 0, opacity: 1 },
        { x: '12vw', opacity: 0, ease: 'power2.in' },
        0.7
      );
    }, section);

    return () => ctx.revert();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="spotlight"
      className="section-pinned bg-[#F6F8F6] z-[80]"
    >
      {/* Left media panel */}
      <div
        ref={leftPanelRef}
        className="absolute left-0 top-0 w-full lg:w-[58vw] h-full"
      >
        <div className="relative w-full h-full image-grade">
          <img
            src="/innovation_lab_films.jpg"
            alt="Compostable film sheets"
            className="w-full h-full object-cover"
          />
        </div>
      </div>

      {/* Right panel */}
      <div
        ref={rightPanelRef}
        className="absolute right-0 top-0 w-full lg:w-[42vw] h-full bg-[#F6F8F6] flex flex-col justify-center px-8 lg:px-[5vw]"
      >
        <div className="flex items-center gap-2 mb-4">
          <Sparkles size={18} className="text-accent" />
          <span className="micro-label">Innovation Spotlight</span>
        </div>

        <h2 className="headline-lg text-3xl sm:text-4xl lg:text-[clamp(34px,3.6vw,56px)] text-primary-dark mb-6">
          Inside the pilot line.
        </h2>

        <p className="body-text text-base text-secondary-muted mb-6 max-w-[30vw]">
          How one materials lab is scaling compostable films—without sacrificing
          clarity or seal strength.
        </p>

        {/* Key innovations */}
        <div className="space-y-3 mb-8">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 bg-accent/10 rounded-md flex items-center justify-center">
              <Beaker size={16} className="text-accent" />
            </div>
            <span className="text-sm text-primary-dark">
              Enhanced barrier properties
            </span>
          </div>
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 bg-accent/10 rounded-md flex items-center justify-center">
              <Award size={16} className="text-accent" />
            </div>
            <span className="text-sm text-primary-dark">
              Industrial compostability certified
            </span>
          </div>
        </div>

        <a
          href="#"
          className="btn-primary inline-flex items-center gap-2 w-fit"
        >
          Read the spotlight
          <ArrowRight size={18} />
        </a>
      </div>
    </section>
  );
};

export default InnovationSpotlightSection;
