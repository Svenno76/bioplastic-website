import { useEffect, useRef } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import Navigation from './sections/Navigation';
import HeroSection from './sections/HeroSection';
import FeaturedStorySection from './sections/FeaturedStorySection';
import BrowseHubSection from './sections/BrowseHubSection';
import MarketStudiesSection from './sections/MarketStudiesSection';
import GlossarySection from './sections/GlossarySection';
import TrendingSection from './sections/TrendingSection';
import TopicsGridSection from './sections/TopicsGridSection';
import InnovationSpotlightSection from './sections/InnovationSpotlightSection';
import NewsletterCTASection from './sections/NewsletterCTASection';
import SubscribeFooterSection from './sections/SubscribeFooterSection';
import './App.css';

gsap.registerPlugin(ScrollTrigger);

function App() {
  const mainRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Global snap for pinned sections
    const setupGlobalSnap = () => {
      const pinned = ScrollTrigger.getAll()
        .filter(st => st.vars.pin)
        .sort((a, b) => a.start - b.start);
      
      const maxScroll = ScrollTrigger.maxScroll(window);
      if (!maxScroll || pinned.length === 0) return;

      const pinnedRanges = pinned.map(st => ({
        start: st.start / maxScroll,
        end: (st.end ?? st.start) / maxScroll,
        center: (st.start + ((st.end ?? st.start) - st.start) * 0.5) / maxScroll,
      }));

      ScrollTrigger.create({
        snap: {
          snapTo: (value: number) => {
            const inPinned = pinnedRanges.some(r => value >= r.start - 0.02 && value <= r.end + 0.02);
            if (!inPinned) return value;

            const target = pinnedRanges.reduce((closest, r) =>
              Math.abs(r.center - value) < Math.abs(closest - value) ? r.center : closest,
              pinnedRanges[0]?.center ?? 0
            );
            return target;
          },
          duration: { min: 0.15, max: 0.35 },
          delay: 0,
          ease: 'power2.out',
        }
      });
    };

    // Delay to allow all ScrollTriggers to initialize
    const timer = setTimeout(setupGlobalSnap, 500);

    return () => {
      clearTimeout(timer);
      ScrollTrigger.getAll().forEach(st => st.kill());
    };
  }, []);

  return (
    <div ref={mainRef} className="relative">
      {/* Grain overlay */}
      <div className="grain-overlay" />
      
      {/* Navigation */}
      <Navigation />
      
      {/* Main content */}
      <main className="relative">
        {/* Section 1: Hero */}
        <HeroSection />
        
        {/* Section 2: Featured Story */}
        <FeaturedStorySection />
        
        {/* Section 3: Browse Hub */}
        <BrowseHubSection />
        
        {/* Section 4: Market Studies */}
        <MarketStudiesSection />
        
        {/* Section 5: Glossary */}
        <GlossarySection />
        
        {/* Section 6: Trending */}
        <TrendingSection />
        
        {/* Section 7: Topics Grid */}
        <TopicsGridSection />
        
        {/* Section 8: Innovation Spotlight */}
        <InnovationSpotlightSection />
        
        {/* Section 9: Newsletter CTA */}
        <NewsletterCTASection />
        
        {/* Section 10: Subscribe + Footer */}
        <SubscribeFooterSection />
      </main>
    </div>
  );
}

export default App;
