import { useRef, useLayoutEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import {
  Scale,
  FlaskConical,
  Package,
  Recycle,
  Truck,
  Rocket,
  Wheat,
  ShoppingBag,
  ArrowRight,
} from 'lucide-react';

gsap.registerPlugin(ScrollTrigger);

const TopicsGridSection = () => {
  const sectionRef = useRef<HTMLElement>(null);
  const titleRef = useRef<HTMLDivElement>(null);
  const cardsRef = useRef<(HTMLDivElement | null)[]>([]);

  const topics = [
    {
      icon: Scale,
      title: 'Policy & Regulation',
      description: 'EU directives, plastic bans, and compliance updates.',
      color: 'bg-blue-50',
    },
    {
      icon: FlaskConical,
      title: 'Material Science',
      description: 'PLA, PHA, bio-PE, and next-gen polymers.',
      color: 'bg-purple-50',
    },
    {
      icon: Package,
      title: 'Packaging Design',
      description: 'Innovations in sustainable packaging solutions.',
      color: 'bg-green-50',
    },
    {
      icon: Recycle,
      title: 'End-of-Life',
      description: 'Composting, recycling, and circular systems.',
      color: 'bg-amber-50',
    },
    {
      icon: Truck,
      title: 'Supply Chain',
      description: 'Feedstock sourcing and logistics optimization.',
      color: 'bg-orange-50',
    },
    {
      icon: Rocket,
      title: 'Startups',
      description: 'Emerging companies and venture funding.',
      color: 'bg-rose-50',
    },
    {
      icon: Wheat,
      title: 'Food & Ag',
      description: 'Agricultural applications and food packaging.',
      color: 'bg-emerald-50',
    },
    {
      icon: ShoppingBag,
      title: 'Consumer Brands',
      description: 'Brand commitments and market adoption.',
      color: 'bg-cyan-50',
    },
  ];

  useLayoutEffect(() => {
    const section = sectionRef.current;
    if (!section) return;

    const ctx = gsap.context(() => {
      // Title animation
      gsap.fromTo(
        titleRef.current,
        { y: 24, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: 0.6,
          scrollTrigger: {
            trigger: titleRef.current,
            start: 'top 80%',
            end: 'top 55%',
            scrub: 0.4,
          },
        }
      );

      // Cards animation
      cardsRef.current.forEach((card, index) => {
        if (card) {
          gsap.fromTo(
            card,
            { y: 40, opacity: 0 },
            {
              y: 0,
              opacity: 1,
              duration: 0.5,
              delay: index * 0.05,
              scrollTrigger: {
                trigger: card,
                start: 'top 85%',
                end: 'top 60%',
                scrub: 0.4,
              },
            }
          );
        }
      });
    }, section);

    return () => ctx.revert();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="topics"
      className="relative bg-[#F6F8F6] py-20 lg:py-32 z-[70]"
    >
      <div className="px-8 lg:px-[8vw]">
        {/* Title block */}
        <div ref={titleRef} className="max-w-[40vw] mb-12">
          <h2 className="headline-lg text-3xl sm:text-4xl lg:text-[clamp(34px,3.6vw,56px)] text-primary-dark mb-4">
            Explore by topic.
          </h2>
          <p className="body-text text-base text-secondary-muted">
            Deep dives into the areas shaping the industry.
          </p>
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6">
          {topics.map((topic, index) => (
            <div
              key={topic.title}
              ref={(el) => { cardsRef.current[index] = el; }}
              className="card-hover bg-white rounded-md p-6 shadow-sm cursor-pointer group"
            >
              <div
                className={`w-12 h-12 ${topic.color} rounded-md flex items-center justify-center mb-4 group-hover:scale-110 transition-transform`}
              >
                <topic.icon size={24} className="text-accent" />
              </div>
              <h3 className="font-heading text-lg font-medium text-primary-dark mb-2">
                {topic.title}
              </h3>
              <p className="body-text text-sm text-secondary-muted mb-4">
                {topic.description}
              </p>
              <div className="flex items-center gap-2 text-sm text-accent opacity-0 group-hover:opacity-100 transition-opacity">
                <span>Explore</span>
                <ArrowRight size={14} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TopicsGridSection;
