export default function Featured() {
  return (
    <div className="flex flex-col lg:flex-row lg:justify-between lg:items-center min-h-screen px-6 py-12 lg:py-0 bg-neutral-950">
      <div className="flex-1 h-[400px] lg:h-[800px] mb-8 lg:mb-0 lg:order-2">
        <img
          src="https://cdn.poehali.dev/projects/a6fd640c-8e26-4822-a39f-c5cde93e3136/files/cc47faa8-d07d-4740-a6c4-d6c84252ef84.jpg"
          alt="Fighting game character"
          className="w-full h-full object-cover"
        />
      </div>
      <div className="flex-1 text-left lg:h-[800px] flex flex-col justify-center lg:mr-12 lg:order-1">
        <h3 className="uppercase mb-4 text-sm tracking-wide text-red-500">Почему наша игра</h3>
        <p className="text-2xl lg:text-4xl mb-8 text-white leading-tight">
          PvP-бои в реальном времени, рейтинговая таблица лучших и сезонные награды — каждый матч решает, кто окажется на вершине.
        </p>
        <div className="flex flex-col gap-4 mb-10">
          <div className="flex items-center gap-3 text-neutral-300">
            <span className="text-red-500 font-bold text-xl">01</span>
            <span className="text-base">Онлайн-бои с живыми игроками по всему миру</span>
          </div>
          <div className="flex items-center gap-3 text-neutral-300">
            <span className="text-red-500 font-bold text-xl">02</span>
            <span className="text-base">Рейтинговая система и сезонные чемпионаты</span>
          </div>
          <div className="flex items-center gap-3 text-neutral-300">
            <span className="text-red-500 font-bold text-xl">03</span>
            <span className="text-base">Уникальные бойцы с особыми приёмами</span>
          </div>
        </div>
        <button className="bg-red-600 text-white border border-red-600 px-6 py-3 text-sm transition-all duration-300 hover:bg-transparent hover:text-red-500 cursor-pointer w-fit uppercase tracking-wide font-bold">
          Вступить в бой
        </button>
      </div>
    </div>
  );
}