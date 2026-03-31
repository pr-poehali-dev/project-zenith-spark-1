import { useScroll, useTransform, motion } from "framer-motion";
import { useRef } from "react";

export default function Hero() {
  const container = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: container,
    offset: ["start start", "end start"],
  });
  const y = useTransform(scrollYProgress, [0, 1], ["0vh", "50vh"]);

  return (
    <div
      ref={container}
      className="relative flex items-center justify-center h-screen overflow-hidden"
    >
      <motion.div
        style={{ y }}
        className="absolute inset-0 w-full h-full"
      >
        <img
          src="https://cdn.poehali.dev/projects/a6fd640c-8e26-4822-a39f-c5cde93e3136/files/5d5057cf-295f-4829-8c1b-0a8ff81bbb3c.jpg"
          alt="Fighting game arena"
          className="w-full h-full object-cover"
        />
      </motion.div>

      <div className="absolute inset-0 bg-black/50 z-[1]" />
      <div className="relative z-10 text-center text-white px-6">
        <p className="text-xs md:text-sm uppercase tracking-[0.3em] mb-4 text-red-400 font-semibold">
          Мобильный файтинг
        </p>
        <h1 className="text-5xl md:text-7xl lg:text-9xl font-black tracking-tight mb-6 uppercase leading-none">
          СРАЗИСЬ<br />ЗА №1
        </h1>
        <p className="text-lg md:text-xl max-w-2xl mx-auto opacity-80 mb-10">
          Реальные бои с живыми игроками. Побеждай в рейтинговых матчах и стань лучшим бойцом сезона.
        </p>
        <button className="bg-red-600 hover:bg-red-700 text-white px-10 py-4 text-sm uppercase tracking-widest font-bold transition-all duration-300 cursor-pointer">
          Скачать игру
        </button>
      </div>
    </div>
  );
}