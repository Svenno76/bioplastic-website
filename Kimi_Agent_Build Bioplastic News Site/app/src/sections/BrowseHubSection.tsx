import { useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ArrowRight, Newspaper, Building2, Calendar } from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const BrowseHubSection = () => {
  const sectionRef = useRef<HTMLElement>(null);
  const leftPanelRef = useRef<HTMLDivElement>(null);
  const cardsRef = useRef<(HTMLDivElement | null)[]>([]);

  const cards = [
    {
      icon: Newspaper,
      title: 'News',
      description: 'Daily updates on materials, policy, and funding.',
      cta: 'Read news',
      href: '#news',
    },
    {
      icon: Building2,
      title: 'Companies',
      description: 'Profiles, partnerships, and plant tours.',
      cta: 'Explore profiles',
      href: '#companies',
    },
    {
      icon: Calendar,
      title: 'Events',
      description: 'Conferences, webinars, and deadlines.',
      cta: 'View calendar',
      href: '#events',
    },
  ];

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
        { x: '-60vw' },
        { x: 0, ease: 'none' },
        0
      );

      cardsRef.current.forEach((card, index) => {
        if (card) {
          scrollTl.fromTo(
            card,
            { x: '50vw', opacity: 0 },
            { x: 0, opacity: 1, ease: 'none' },
            index * 0.06
          );
        }
      });

      // SETTLE (30%-70%): Hold

      // EXIT (70%-100%)
      scrollTl.fromTo(
        leftPanelRef.current,
        { x: 0, opacity: 1 },
        { x: '-14vw', opacity: 0.3, ease: 'power2.in' },
        0.7
      );

      cardsRef.current.forEach((card) => {
        if (card) {
          scrollTl.fromTo(
            card,
            { x: 0, opacity: 1 },
            { x: '8vw', opacity: 0, ease: 'power2.in' },
            0.7
          );
        }
      });
    }, section);

    return () => ctx.revert();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="browse"
      className="section-pinned bg-[#F6F8F6] z-30"
    >
      {/* Left media panel */}
      <div
        ref={leftPanelRef}
        className="absolute left-0 top-0 w-full lg:w-[58vw] h-full"
      >
        <div className="relative w-full h-full image-grade">
          <img
            src="/browse_hub_leaves.jpg"
            alt="Green leaves with water droplets"
            className="w-full h-full object-cover"
          />
        </div>
      </div>

      {/* Right cards panel */}
      <div className="absolute right-0 top-0 w-full lg:w-[42vw] h-full bg-[#F6F8F6] flex flex-col justify-center px-8 lg:px-[4vw]">
        <div className="space-y-4 lg:space-y-6">
          {cards.map((card, index) => (
            <div
              key={card.title}
              ref={(el) => { cardsRef.current[index] = el; }}
              className="card-hover bg-white rounded-md p-5 lg:p-6 shadow-sm cursor-pointer"
            >
              <div className="flex items-start gap-4">
                <div className="p-2 bg-accent/10 rounded-md">
                  <card.icon size={24} className="text-accent" />
                </div>
                <div className="flex-1">
                  <h3 className="font-heading text-xl font-medium text-primary-dark mb-2">
                    {card.title}
                  </h3>
                  <p className="body-text text-sm text-secondary-muted mb-3">
                    {card.description}
                  </p>
                  <a
                    href={card.href}
                    className="inline-flex items-center gap-2 text-sm font-medium text-accent hover:underline"
                  >
                    {card.cta}
                    <ArrowRight size={14} />
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default BrowseHubSection;
