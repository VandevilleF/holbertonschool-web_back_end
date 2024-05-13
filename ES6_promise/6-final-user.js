import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userP = signUpUser(firstName, lastName);
  const photoP = uploadPhoto(fileName);
  const results = await Promise.allSettled([userP, photoP]);
  return results.map((result) => ({
    status: result.status,
    value: result.status === 'fulfilled' ? result.value : `Error: ${result.reason.message}`,
  }));
}
