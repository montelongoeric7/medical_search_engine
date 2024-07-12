import React, { useState } from 'react';
import {
  Box,
  Heading,
  FormControl,
  FormLabel,
  Input,
  Button,
  VStack,
  useToast,
  Image,
  Text,
} from '@chakra-ui/react';
import { FaFileUpload } from 'react-icons/fa';

const UpdateData = () => {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState('');
  const toast = useToast();

  const handleFileChange = (event) => {
    const uploadedFile = event.target.files[0];
    setFile(uploadedFile);
    setFileName(uploadedFile.name);
  };

  const handleFileUpload = async () => {
    try {
      const token = localStorage.getItem('token');
      if (!token) {
        throw new Error('No token found');
      }

      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch('http://localhost:8000/information/upload-pdf', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to upload PDF');
      }

      const data = await response.json();
      toast({
        title: 'PDF uploaded.',
        description: `Your PDF has been uploaded and summarized.`,
        status: 'success',
        duration: 5000,
        isClosable: true,
      });
    } catch (error) {
      console.error('Error uploading PDF:', error);
      toast({
        title: 'Error.',
        description: "There was an error uploading your PDF.",
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    }
  };

  return (
    <Box textAlign="center" py={10} px={6} bg="gray.50" minH="100vh">
      <Heading as="h2" size="xl" mb={6} color="teal.500">
        Upload Your PDF
      </Heading>
      <VStack spacing={4} align="center" width="100%" maxWidth="500px" mx="auto" p={6} boxShadow="lg" bg="white" borderRadius="lg">
        <FormControl id="pdf" isRequired>
          <FormLabel>Choose PDF</FormLabel>
          <Input
            type="file"
            accept="application/pdf"
            onChange={handleFileChange}
            p={1}
          />
        </FormControl>
        {fileName && (
          <Text fontSize="md" color="gray.600">
            Selected file: {fileName}
          </Text>
        )}
        <Button
          leftIcon={<FaFileUpload />}
          colorScheme="teal"
          bg="teal.400"
          _hover={{ bg: 'teal.500' }}
          rounded="full"
          onClick={handleFileUpload}
          isDisabled={!file}
        >
          Upload PDF
        </Button>
      </VStack>
      {file && (
        <Image
          src={URL.createObjectURL(file)}
          alt="Selected PDF"
          mt={6}
          maxWidth="100%"
          borderRadius="lg"
          boxShadow="md"
        />
      )}
    </Box>
  );
};

export default UpdateData;
