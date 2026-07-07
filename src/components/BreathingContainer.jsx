import { motion } from "framer-motion";

export default function BreathingContainer({ children }) {
  return (
    <motion.div
      animate={{
        scale: [1, 1.01, 1],
      }}
      transition={{
        duration: 6,
        repeat: Infinity,
        ease: "easeInOut",
      }}
      style={{
        width: "100%",
        height: "100%",
      }}
    >
      {children}
    </motion.div>
  );
}