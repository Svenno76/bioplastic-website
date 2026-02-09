import { useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight, TrendingUp, BarChart3, FileText } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const MarketStudiesSection = () => {
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

  return (
    <section
      ref={sectionRef}
      id="studies"
      className="section-pinned bg-[#F6F8F6] z-40"
    >
      {/* Left text panel */}
      <div
        ref={leftPanelRef}
        className="absolute left-0 top-0 w-full lg:w-[42vw] h-full bg-[#F6F8F6] flex flex-col justify-center px-8 lg:px-[8vw]"
      >
        <h2 className="headline-lg text-3xl sm:text-4xl lg:text-[clamp(34px,3.6vw,56px)] text-primary-dark mb-6">
          Data that moves decisions.
        </h2>

        <p className="body-text text-base text-secondary-muted mb-8 max-w-[30vw]">
          Capacity maps, price indices, and policy briefs—updated monthly.
        </p>

        {/* Stats preview */}
        <div className="grid grid-cols-2 gap-4 mb-8">
          <div className="bg-white rounded-md p-4 shadow-sm">
            <div className="flex items-center gap-2 mb-2">
              <TrendingUp size={18} className="text-accent" />
              <span className="micro-label">Growth</span>
            </div>
            <p className="font-heading text-2xl font-medium text-primary-dark">
              17.5%
            </p>
            <p className="text-xs text-secondary-muted">CAGR 2025-2035</p>
          </div>
          <div className="bg-white rounded-md p-4 shadow-sm">
            <div className="flex items-center gap-2 mb-2">
              <BarChart3 size={18} className="text-accent" />
              <span className="micro-label">Market</span>
            </div>
            <p className="font-heading text-2xl font-medium text-primary-dark">
              $23.8B
            </p>
            <p className="text-xs text-secondary-muted">2025 Value</p>
          </div>
        </div>

        <a
          href="#"
          className="btn-primary inline-flex items-center gap-2 w-fit"
        >
          Browse studies
          <ArrowRight size={18} />
        </a>
      </div>

      {/* Right media panel */}
      <div
        ref={rightPanelRef}
        className="absolute right-0 top-0 w-full lg:w-[58vw] h-full"
      >
        <div className="relative w-full h-full image-grade">
          <img
            src="/market_studies_tablet.jpg"
            alt="Tablet with data on desk"
            className="w-full h-full object-cover"
          />
          {/* Floating stat card */}
          <div className="absolute bottom-8 left-8 bg-white/95 backdrop-blur-sm rounded-md p-4 shadow-lg max-w-[240px]">
            <div className="flex items-center gap-2 mb-2">
              <FileText size={16} className="text-accent" />
              <span className="micro-label">Latest Report</span>
            </div>
            <p className="font-heading text-sm font-medium text-primary-dark">
              Bioplastics Market Development Update 2025
            </p>
            <p className="text-xs text-secondary-muted mt-1">
              European Bioplastics / nova-Institute
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default MarketStudiesSection;
