import React from 'react';
import { Box, Heading, Text, Image, VStack, HStack } from '@chakra-ui/react';
import contactImage from '../assets/CityTwo.png'; // Ensure you have an image in the assets folder

const Contact = () => {
  return (
    <Box textAlign="center" py={10} px={6}>
      <Heading as="h1" size="2xl" mb={6}>
        Feel Free to Contact Us!!!
      </Heading>
      <HStack justify="center" mb={6}>
        <Image
          src={contactImage}
          alt="Contact Us"
          borderRadius="full"
          boxSize="150px"
        />
      </HStack>
      <VStack spacing={4} align="center">
        <Text fontSize="lg">
          We would love to hear from you! If you have any questions, feedback, or inquiries, please reach out to us. Here is our information:
        </Text>
        <Text fontSize="md" color="gray.600">
          Email: mediconnect@gmail.com or mediconnext@yahoo.com
        </Text>
        <Text fontSize="md" color="gray.600">
          Phone: (123) 456-7890
        </Text>
        <Text fontSize="md" color="gray.600">
          Address: 123 Main Street, Los Angeles CA, USA
          Address: Remote
        </Text>
      </VStack>
    </Box>
  );
};

export default Contact;
