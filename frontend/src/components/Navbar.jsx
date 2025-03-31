import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-gray-900 text-white p-4 flex justify-between">
      <h1 className="text-xl font-bold">Deep Learning App</h1>
      <div>
        <Link className="mr-4" to="/">Classification</Link>
        <Link to="/denoising">Denoising</Link>
        
      </div>
    </nav>
  );
};

export default Navbar;
