import { motion } from "framer-motion";

const blobs = [
  {
    size: 420,
    color: "#66D9FF",
    top: "8%",
    left: "-10%",
    duration: 18,
    x: [0, 80, -40, 0],
    y: [0, 50, -60, 0],
    scale: [1, 1.12, 0.95, 1],
  },
  {
    size: 360,
    color: "#6C63FF",
    top: "55%",
    left: "55%",
    duration: 20,
    x: [0, -70, 60, 0],
    y: [0, -50, 30, 0],
    scale: [1, 0.9, 1.15, 1],
  },
  {
    size: 300,
    color: "#2EE6A6",
    top: "15%",
    left: "65%",
    duration: 16,
    x: [0, 40, -60, 0],
    y: [0, 60, -40, 0],
    scale: [1, 1.18, 0.88, 1],
  },
  {
    size: 250,
    color: "#8FD8FF",
    top: "72%",
    left: "18%",
    duration: 22,
    x: [0, 60, -30, 0],
    y: [0, -60, 40, 0],
    scale: [1, 1.08, 0.92, 1],
  },
];

function Blob({
  size,
  color,
  top,
  left,
  duration,
  x,
  y,
  scale,
}) {
  return (
    <motion.div
      style={{
        position: "absolute",
        width: size,
        height: size,
        top,
        left,
        borderRadius: "45% 55% 58% 42% / 45% 35% 65% 55%",
        background: color,
        filter: "blur(90px)",
        opacity: 0.55,
        mixBlendMode: "screen",
      }}
      animate={{
        x,
        y,
        scale,
        rotate: [0, 15, -10, 0],
        borderRadius: [
          "45% 55% 58% 42% / 45% 35% 65% 55%",
          "58% 42% 40% 60% / 35% 65% 45% 55%",
          "40% 60% 55% 45% / 55% 35% 65% 45%",
          "45% 55% 58% 42% / 45% 35% 65% 55%",
        ],
      }}
      transition={{
        duration,
        ease: "easeInOut",
        repeat: Infinity,
      }}
    />
  );
}

export default function AIBackground() {
  return (
    <div
      style={{
        position: "relative",
        width: "100%",
        height: "100vh",
        overflow: "hidden",
        background:
          "linear-gradient(180deg,#eefaf5 0%,#eaf8ff 45%,#f3fdf8 100%)",
      }}
    >
      {/* SVG Filters */}
      <svg width="0" height="0">
        <defs>
          <filter id="noise">
            <feTurbulence
              type="fractalNoise"
              baseFrequency="0.75"
              numOctaves="3"
              stitchTiles="stitch"
            />
            <feColorMatrix
              type="saturate"
              values="0"
            />
          </filter>
        </defs>
      </svg>

      {/* Animated Blobs */}
      {blobs.map((blob, i) => (
        <Blob key={i} {...blob} />
      ))}

      {/* Radial Glow */}
      <motion.div
        animate={{
          scale: [1, 1.12, 1],
          opacity: [0.25, 0.4, 0.25],
        }}
        transition={{
          duration: 8,
          repeat: Infinity,
          ease: "easeInOut",
        }}
        style={{
          position: "absolute",
          width: 900,
          height: 900,
          left: "50%",
          top: "50%",
          transform: "translate(-50%,-50%)",
          background:
            "radial-gradient(circle, rgba(255,255,255,.7), transparent 70%)",
          filter: "blur(120px)",
        }}
      />

      {/* Noise Layer */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          filter: "url(#noise)",
          opacity: 0.05,
          mixBlendMode: "soft-light",
          pointerEvents: "none",
        }}
      />

      {/* Content */}
      <div
        style={{
          position: "relative",
          zIndex: 20,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100%",
          flexDirection: "column",
          color: "#222",
        }}
      >
        <motion.h1
          animate={{
            opacity: [0.5, 1, 0.5],
            y: [0, -6, 0],
          }}
          transition={{
            duration: 2.5,
            repeat: Infinity,
          }}
          style={{
            fontSize: 40,
            fontWeight: 600,
            letterSpacing: -1,
          }}
        >
          Generating Image...
        </motion.h1>
      </div>
    </div>
  );
}