document.addEventListener('DOMContentLoaded', function() {
    const baseURL = 'mysql+mysqlconnector://root:admin@localhost:3306/tpi';


    async function getTotalEvents() {
        try {
            const response = await axios.get(`${baseURL}/events`);
            document.getElementById('totalEvents').textContent = response.data.length;
        } catch (error) {
            console.error('Error fetching total events:', error);
        }
    }


    async function getTotalActiveInscriptions() {
        try {
            const response = await axios.get(`${baseURL}/inscriptions/active`);
            document.getElementById('totalActiveInscriptions').textContent = response.data.length;
        } catch (error) {
            console.error('Error fetching total active inscriptions:', error);
        }
    }


    async function getAverageUsersPerEvent() {
        try {
            const responseEvents = await axios.get(`${baseURL}/events`);
            const responseInscriptions = await axios.get(`${baseURL}/inscriptions`);

            const averageUsers = responseInscriptions.data.length / responseEvents.data.length;
            document.getElementById('averageUsersPerEvent').textContent = averageUsers.toFixed(2);
        } catch (error) {
            console.error('Error fetching average users per event:', error);
        }
    }


    async function getEventWithMostInscriptions() {
        try {
            const response = await axios.get(`${baseURL}/events`);
            let maxInscriptions = 0;
            let eventWithMostInscriptions = '';

            response.data.forEach(event => {
                if (event.inscriptions.length > maxInscriptions) {
                    maxInscriptions = event.inscriptions.length;
                    eventWithMostInscriptions = event.name;
                }
            });

            document.getElementById('eventWithMostInscriptions').textContent = eventWithMostInscriptions;
        } catch (error) {
            console.error('Error fetching event with most inscriptions:', error);
        }
    }


    getTotalEvents();
    getTotalActiveInscriptions();
    getAverageUsersPerEvent();
    getEventWithMostInscriptions();
});
