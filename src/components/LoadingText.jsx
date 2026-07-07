import { motion } from "framer-motion";

export default function LoadingText() {

    return (

        <motion.div

            animate={{
                opacity:[.35,1,.35]
            }}

            transition={{
                repeat:Infinity,
                duration:2.2
            }}

            style={{
                position:"absolute",
                left:"50%",
                top:"50%",
                translate:"-50% -50%",
                fontSize:36,
                fontWeight:600,
                color:"#1f2937"
            }}

        >

            Generating Image...

        </motion.div>

    )

}