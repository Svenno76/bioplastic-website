import { useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const FeaturedStorySection = () => {
  const sectionRef = useRef<HTMLElement>(null);
  const leftPanelRef = useRef<HTMLDivElement>(null);
  const rightPanelRef = useRef<HTMLDivElement>(null);
  const headlineRef = useRef<HTMLHeadingElement>(null);
  const bodyRef = useRef<HTMLParagraphElement>(null);
  const ctaRef = useRef<HTMLAnchorElement>(null);

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
        { x: '-18vw', opacity: 0, ease: 'power2.in' },
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
      id="featured"
      className="section-pinned bg-[#F6F8F6] z-20"
    >
      {/* Left media panel */}
      <div
        ref={leftPanelRef}
        className="absolute left-0 top-0 w-full lg:w-[62vw] h-full"
      >
        <div className="relative w-full h-full image-grade">
          <img
            src="/featured_bottle_pour.jpg"
            alt="Bottle pouring liquid"
            className="w-full h-full object-cover"
          />
        </div>
      </div>

      {/* Right text panel */}
      <div
        ref={rightPanelRef}
        className="absolute right-0 top-0 w-full lg:w-[38vw] h-full bg-[#F6F8F6] flex flex-col justify-center px-8 lg:px-[5vw]"
      >
        <h2
          ref={headlineRef}
          className="headline-lg text-3xl sm:text-4xl lg:text-[clamp(34px,3.6vw,56px)] text-primary-dark mb-6"
        >
          The field-to-bottle experiment.
        </h2>

        <p
          ref={bodyRef}
          className="body-text text-base text-secondary-muted mb-8 max-w-[28vw]"
        >
          A small farm coalition is testing straw-derived barriers for beverage
          cartons—measuring performance, cost, and carbon.
        </p>

        <a
          ref={ctaRef}
          href="#"
          className="btn-primary inline-flex items-center gap-2 w-fit"
        >
          Read the feature
          <ArrowRight size={18} />
        </a>
      </div>
    </section>
  );
};

export default FeaturedStorySection;
