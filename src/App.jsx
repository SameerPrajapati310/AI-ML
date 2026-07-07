import { useState } from "react";

import AIBackground from "./components/AIBackground";
import ImageReveal from "./components/ImageReveal";

export default function App() {

  const [loading, setLoading] = useState(false);
  const [image, setImage] = useState("");

  async function generateImage() {

    setLoading(true);

    setImage("");

    /*
      Replace this timeout with your API call.
    */

    await new Promise((resolve) =>
      setTimeout(resolve, 4500)
    );

    setImage(
      "https://images.unsplash.com/photo-1682686580391-615b1f28e9e1?w=1200"
    );

    setLoading(false);
  }

  return (

    <div
      style={{
        width: "100vw",
        height: "100vh",
      }}
    >

      <AIBackground />

      <ImageReveal
        image={image}
        loading={loading}
      />

      <button
        onClick={generateImage}
        style={{
          position: "absolute",
          bottom: 40,
          left: "50%",
          transform: "translateX(-50%)",
          padding: "14px 26px",
          borderRadius: 14,
          border: 0,
          background: "#111827",
          color: "white",
          cursor: "pointer",
          fontSize: 16,
        }}
      >
        Generate
      </button>

    </div>

  );
}