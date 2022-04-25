import { useEffect, useState } from 'react';

function ListCourses() {
  const [courses, setCourses] = useState([]);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const username = process.env.REACT_APP_API_USERNAME;
    const password = process.env.REACT_APP_API_PASSWORD;
    
    const headers = new Headers();
    const authorizationToken = Buffer.from(`${username}:${password}`).toString('base64');
    headers.set('Authorization', `Basic ${authorizationToken}`)
    
    fetch(`${process.env.REACT_APP_BASE_API_URL}/courses/`, {
        headers: headers,
    })
      .then((res) => {
        if (!res.ok) {
          // Something went wrong, do whatever you want with it (good luck).
        }

        return res.json();
      })
      .then((data) => setCourses(data.results))
      .catch((err) => console.error(err))
      .finally(() => setLoaded(true));
  }, []);

  if (!loaded) {
    return <h1>Carregando...</h1>;
  }

  return (
    <>
      {courses.map((course) => {
        return (
          <h2 key={course.id} className="App-table">
            {course.description}
          </h2>
        );
      })}
    </>
  );
}

export default ListCourses;
