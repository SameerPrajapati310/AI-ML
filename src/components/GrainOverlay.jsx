import { motion } from "framer-motion";

export default function GrainOverlay() {
  return (
    <>
      <svg width="0" height="0">
        <filter id="grainFilter">
          <feTurbulence
            type="fractalNoise"
            baseFrequency="0.85"
            numOctaves="3"
            stitchTiles="stitch"
            result="noise"
          />

          <feColorMatrix
            type="saturate"
            values="0"
          />

          <feComponentTransfer>
            <feFuncA
              type="table"
              tableValues="0 0.05"
            />
          </feComponentTransfer>
        </filter>
      </svg>

      <motion.div
        animate={{
          x: [0, -40, 20, 0],
          y: [0, 25, -15, 0],
        }}
        transition={{
          duration: 15,
          repeat: Infinity,
          ease: "linear",
        }}
        style={{
          position: "absolute",
          inset: "-20%",
          filter: "url(#grainFilter)",
          opacity: .45,
          mixBlendMode: "soft-light",
          pointerEvents: "none",
        }}
      />
    </>
  );
}