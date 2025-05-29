
import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await axios.post('http://localhost:8000/upload/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });

    console.log(response.data);
  };

  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default UploadForm;
