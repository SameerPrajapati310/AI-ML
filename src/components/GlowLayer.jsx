import { motion } from "framer-motion";

export default function GlowLayer() {
  return (
    <>
      <motion.div
        className="glow glow1"
        animate={{
          scale: [1, 1.18, 1],
          opacity: [.25, .45, .25],
          x: [0, 50, 0],
          y: [0, -40, 0],
        }}
        transition={{
          duration: 12,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />

      <motion.div
        className="glow glow2"
        animate={{
          scale: [1, .92, 1.15, 1],
          opacity: [.2, .4, .2],
          x: [0, -60, 40, 0],
          y: [0, 50, -40, 0],
        }}
        transition={{
          duration: 16,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
    </>
  );
}