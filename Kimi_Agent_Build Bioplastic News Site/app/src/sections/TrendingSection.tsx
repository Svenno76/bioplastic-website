import { useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight, Coffee, Users, Lightbulb } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const TrendingSection = () => {
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
        { x: '70vw' },
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
        { x: '16vw', opacity: 0.35, ease: 'power2.in' },
        0.7
      );
    }, section);

    return () => ctx.revert();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="trending"
      className="section-pinned bg-[#F6F8F6] z-[60]"
    >
      {/* Left text panel */}
      <div
        ref={leftPanelRef}
        className="absolute left-0 top-0 w-full lg:w-[40vw] h-full bg-[#F6F8F6] flex flex-col justify-center px-8 lg:px-[8vw]"
      >
        <h2 className="headline-lg text-3xl sm:text-4xl lg:text-[clamp(34px,3.6vw,56px)] text-primary-dark mb-6">
          Culture, curated.
        </h2>

        <p className="body-text text-base text-secondary-muted mb-8 max-w-[30vw]">
          Conversations with designers, chefs, and farmers rethinking materials.
        </p>

        {/* Featured interviews preview */}
        <div className="space-y-3 mb-8">
          <div className="flex items-center gap-3 p-3 bg-white rounded-md shadow-sm">
            <Coffee size={18} className="text-accent" />
            <span className="text-sm text-primary-dark">
              Chef Maria Lopez on compostable packaging
            </span>
          </div>
          <div className="flex items-center gap-3 p-3 bg-white rounded-md shadow-sm">
            <Users size={18} className="text-accent" />
            <span className="text-sm text-primary-dark">
              Farmers alliance for bio-feedstock
            </span>
          </div>
          <div className="flex items-center gap-3 p-3 bg-white rounded-md shadow-sm">
            <Lightbulb size={18} className="text-accent" />
            <span className="text-sm text-primary-dark">
              Designers reshaping product lifecycle
            </span>
          </div>
        </div>

        <a
          href="#"
          className="btn-primary inline-flex items-center gap-2 w-fit"
        >
          Explore trending
          <ArrowRight size={18} />
        </a>
      </div>

      {/* Right media panel */}
      <div
        ref={rightPanelRef}
        className="absolute right-0 top-0 w-full lg:w-[60vw] h-full"
      >
        <div className="relative w-full h-full image-grade">
          <img
            src="/trending_coffee_portrait.jpg"
            alt="Person with coffee cup"
            className="w-full h-full object-cover"
          />
        </div>
      </div>
    </section>
  );
};

export default TrendingSection;
