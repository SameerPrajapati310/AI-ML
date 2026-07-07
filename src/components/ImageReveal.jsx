import { AnimatePresence, motion } from "framer-motion";

export default function ImageReveal({
  image,
  loading,
}) {
  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        overflow: "hidden",
        borderRadius: 24,
      }}
    >
      <AnimatePresence mode="wait">

        {loading && (
          <motion.div
            key="loader"
            initial={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{
              duration: 0.8,
            }}
            style={{
              position: "absolute",
              inset: 0,
            }}
          />
        )}

      </AnimatePresence>

      <AnimatePresence>

        {!loading && image && (

          <motion.img
            key={image}
            src={image}
            alt="generated"

            initial={{
              opacity: 0,
              scale: 1.05,
              filter: "blur(30px)",
              clipPath: "inset(100% 0% 0% 0%)",
            }}

            animate={{
              opacity: 1,
              scale: 1,
              filter: "blur(0px)",
              clipPath: "inset(0% 0% 0% 0%)",
            }}

            exit={{
              opacity: 0,
            }}

            transition={{
              duration: 1.6,
              ease: [0.22, 1, 0.36, 1],
            }}

            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
            }}
          />
        )}

      </AnimatePresence>
    </div>
  );
}